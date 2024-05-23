from typing import List, Optional
from redis_om import Field
from src.models.utility.base_redis_model import BaseRedisModel


class User(BaseRedisModel):
    telegram_id: str = Field(index=True, primary_key=True)
    name: Optional[str] = Field(index=True)
    server_ids: Optional[List[str]] = Field(index=True, default=[])

    class Meta:  # type: ignore
        model_key_prefix = "users"
