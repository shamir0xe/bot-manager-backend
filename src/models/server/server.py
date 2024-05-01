from typing import List, Optional
from redis_om import Field
from src.models.utility.base_redis_model import BaseRedisModel


class Server(BaseRedisModel):
    address: str = Field(index=True)
    port: Optional[int] = Field(index=True, default=443)
    owner_id: str = Field(index=True)
    server_ids: Optional[List[str]] = Field(index=True, default=[])

    class Meta:  # type: ignore
        model_key_prefix = "servers"
