from nonebot import get_bot, get_plugin_config, logger
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.adapters.console import MessageEvent as MessageEventConsole, Bot as ConsoleBot
from nonebot.adapters.onebot.v11 import MessageEvent as MessageEventOnebotv11, GroupMessageEvent as GroupMessageEventOnebotv11, Bot as Onebotv11
from nonebot.params import CommandArg

from nonebot_plugin_apscheduler import scheduler

from .sunsetbot import SunsetBot, ForecastResult
from .db import db
from .config import Config

from typing import List, Union

MessageEvent = Union[MessageEventConsole, MessageEventOnebotv11]


sunset_api = SunsetBot()
config = get_plugin_config(Config).sunsetbot


def forecast_result_output(city: str, result: Union[ForecastResult, List[ForecastResult]], time_format: str = '%Y-%m-%d %H:%M:%S') -> str:
    if isinstance(result, list):
        return f"{city}的火烧云预报：\n" + "\n\n".join(
            f"{r.event_time.strftime(time_format)}\n鲜艳度：{r.quality}\n气溶胶：{r.aod}" for r in result)
    else:
        return f"{city}在{result.event_time.strftime(time_format)}的火烧云预报：\n" \
            f"鲜艳度：{result.quality}\n气溶胶：{result.aod}"


def sunset_query_handler(event_type: str):
    async def handler(matcher: Matcher, args: Message = CommandArg()):
        city = args.extract_plain_text()

        try:
            if event_type == '1day':
                result = await sunset_api.get_forecast_1day(city)
            else:
                result = await sunset_api.get_forecast(city, event_type)
        except Exception as e:
            await matcher.finish(f"查询失败: {e}")
        else:
            await matcher.finish(forecast_result_output(city, result))
    return handler


async def city_query_handler(matcher: Matcher, args: Message = CommandArg()):
    city = args.extract_plain_text()
    try:
        city_list = await sunset_api.query_city(city)
    except Exception as e:
        await matcher.finish(f"查询失败: {e}")
    else:
        if not city_list:
            await matcher.finish("未找到相关城市")
        else:
            await matcher.finish("查询结果：\n"+"\n".join(city_list))


class Context:
    def __init__(self, user_id: str, group_id: str = "-1"):
        self.user_id = user_id
        self.group_id = group_id

    @classmethod
    def from_event(cls, event: MessageEvent):
        if isinstance(event, MessageEventConsole):
            return cls("USER_CONSOLE", "GROUP_CONSOLE")
        elif isinstance(event, GroupMessageEventOnebotv11):
            return cls(event.user_id, event.group_id)
        else:
            return cls(event.user_id)


async def add_schduler_handler(matcher: Matcher, event: MessageEvent, args: Message = CommandArg()):
    context = Context.from_event(event)
    city = args.extract_plain_text()
    schedule_exist = await db.fetch("SELECT id FROM schedule WHERE city=(?) AND user_id=(?) AND group_id=(?)",
                                    (city, context.user_id, context.group_id))
    if schedule_exist:
        await matcher.finish("已订阅过")

    job_id = await db.insert_schedule(city, context.user_id, context.group_id)
    scheduler.add_job(sunset_query_schedule_job, id=str(job_id), args=(city, context.user_id, context.group_id),
                      trigger=config.schedule_trigger, **config.schedule_kwargs)
    await matcher.finish(f"已订阅{city}的火烧云预报，{config.schedule_message}更新")


async def list_user_schedule(matcher: Matcher, event: MessageEvent):
    context = Context.from_event(event)
    schedules = await db.fetch("SELECT id,city FROM schedule WHERE user_id=(?) AND group_id=(?)", (context.user_id, context.group_id))

    user = f"[CQ:at,qq={context.user_id}]" if context.group_id is not None else "你"
    if not schedules:
        await matcher.finish(f"{user}无订阅")
    
    await matcher.finish(f"{user}的订阅：\n"+"\n".join(f"{s[0]}. {s[1]}" for s in schedules))


async def delete_user_schedule(matcher: Matcher, event: MessageEvent, args: Message = CommandArg()):
    context = Context.from_event(event)
    delete_id = args.extract_plain_text()
    delete_city = await db.fetch("SELECT city FROM schedule WHERE id=(?) AND user_id=(?) AND group_id=(?)",
                                 (delete_id, context.user_id, context.group_id))
    if not delete_city:
        await matcher.finish(f"你的订阅中无ID：{delete_id}")

    await db.delete_schedule(delete_id)
    scheduler.remove_job(delete_id)
    await matcher.finish(f"已取消{delete_city[0][0]}的订阅")


async def sunset_query_schedule_job(city: str, user_id: str, group_id: str = None):
    bot: Union[ConsoleBot, Onebotv11] = get_bot()
    
    if isinstance(bot, ConsoleBot):
        # 测试用
        from nonebot.adapters.console import Message as MessageConsoleAdapter
        await bot.send_msg(user_id=user_id, message=MessageConsoleAdapter(
            f"fire schedule: user_id={user_id}, group_id={group_id}, city={city}"))
    else:
        results = await sunset_api.get_forecast_1day(city)
        if group_id:
            msg = f"[CQ:at,qq={user_id}]的订阅：\n" + forecast_result_output(city, results)
            await bot.send_group_msg(group_id=group_id, message=msg)
        else:
            await bot.send_private_msg(user_id=user_id, message=forecast_result_output(city, results))


async def on_startup():
    await db.async_init()

    all_schedule = await db.get_all_schedule()
    for schedule in all_schedule:
        logger.info(f"load job ID {schedule.id} from disk: user_id={schedule.user_id}, group_id={schedule.group_id}, city={schedule.city}")
        scheduler.add_job(sunset_query_schedule_job, id=str(schedule.id), args=(schedule.city, schedule.user_id, schedule.group_id),
                          trigger=config.schedule_trigger, **config.schedule_kwargs)
    
    scheduler.get_jobs()


async def on_end():
    await db.close()
