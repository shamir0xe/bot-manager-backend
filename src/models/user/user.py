from typing import List, Optional
from redis_om import Field, JsonModel
from src.models.utility.base_redis_meta_class import BaseRedisMetaClass


class User(JsonModel):
    telegram_id: str = Field(index=True)
    name: Optional[str] = Field(index=True)
    server_ids: Optional[List[str]] = Field(index=True, default=[])

    class Meta(BaseRedisMetaClass):
        model_key_prefix = "users"
