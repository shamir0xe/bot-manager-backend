from typing import Optional
from redis_om import Field, JsonModel
from src.models.utility.base_redis_meta_class import BaseRedisMetaClass


class Bot(JsonModel):
    id: str = Field(index=True, primary_key=True)
    name: str
    token: str
    host: Optional[str]
    port: Optional[int]
    pages: Optional[str]

    class Meta(BaseRedisMetaClass):
        model_key_prefix = "bots"
