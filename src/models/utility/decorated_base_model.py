from pydantic import BaseModel, Field
from datetime import datetime
from src.actions.utility.get_current_time import GetCurrentTime


class DecoratedBaseModel(BaseModel):
    created_at: datetime = Field(default_factory=GetCurrentTime.get)
    updated_at: datetime = Field(default_factory=GetCurrentTime.get)
