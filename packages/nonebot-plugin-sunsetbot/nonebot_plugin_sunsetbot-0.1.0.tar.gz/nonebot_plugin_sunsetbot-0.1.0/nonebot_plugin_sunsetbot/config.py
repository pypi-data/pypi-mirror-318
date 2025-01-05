from pydantic import BaseModel
from typing import Dict, Optional


class ScopedConfig(BaseModel):
    schedule_trigger: str = "cron"
    schedule_kwargs: Dict = {"hour": "14,21"}
    schedule_message: str = "每日14:00和21:00"


class Config(BaseModel):
    sunsetbot: ScopedConfig = ScopedConfig()