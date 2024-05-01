from abc import ABC
from typing import Optional
from redis_om import Field, JsonModel, get_redis_connection
from datetime import datetime
from src.facades.env import Env


redis = get_redis_connection(url=f"redis://{Env().db.host}:{Env().db.port}/0")


class BaseRedisModel(JsonModel, ABC):
    created_at: Optional[datetime] = Field(index=True, default=None)
    updated_at: Optional[datetime] = Field(index=True, default=None)

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.updated_at = now
        if not self.created_at:
            self.created_at = now

        return super().save(*args, **kwargs)

    class Meta:
        global_key_prefix = Env().project_name
        database = redis
        # model_key_prefix = "base_redis_model"
