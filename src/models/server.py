from typing import List, Optional
from redis_om import Field, JsonModel


class Server(JsonModel):
    address: str = Field(index=True)
    port: Optional[int] = Field(index=True, default=443)
    owner_id: str = Field(index=True)
    server_ids: Optional[List[str]] = Field(index=True, default=[])
