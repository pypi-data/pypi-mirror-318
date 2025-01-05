# nonebot-plugin-sunsetbot

## 功能

查询[Sunsetbot网站](https://sunsetbot.top/)并订阅特定地区通知。

命令：
- 特定时间预报：[今天/明天][朝霞/晚霞] [地区名]
  - 地名精确到市或区，需精确匹配。如：今天朝霞 上海；今天朝霞 上海-徐汇区
- 未来一天预报：火烧云 [地区名]
- 查询地区名：火烧云地区 [部分地区名]
- 每日定时提醒某地区火烧云状态：火烧云订阅 [地区名]
  - 查看订阅列表：火烧云订阅 查看
  - 取消订阅：火烧云订阅 [取消/删除] [地区名]

## 配置

定时提醒配置：
- `SUNSETBOT__SCHEDULE_TRIGGER`：`APScheduler`的`trigger`，默认为`"cron"`
- `SUNSETBOT__SCHEDULE_KWARGS`：设置具体的提醒方式。默认为`{"hour":"14,21"}`，即在每天的14:00、21:00提醒
- `SUNSETBOT__SCHEDULE_MESSAGE`：订阅提醒时向用户发送的信息，与上一项配置对应。默认为`""每日14:00和21:00`