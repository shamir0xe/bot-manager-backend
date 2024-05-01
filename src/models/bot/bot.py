from typing import Optional
from redis_om import Field
from src.models.utility.base_redis_model import BaseRedisModel


class Bot(BaseRedisModel):
    id: str = Field(index=True, primary_key=True)
    name: str
    token: str
    host: Optional[str]
    port: Optional[int]
    pages: Optional[str]

    class Meta:  # type: ignore
        model_key_prefix = "bots"
