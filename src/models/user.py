from typing import List, Optional
from redis_om import Field, JsonModel


class User(JsonModel):
    telegram_id: str = Field(index=True)
    name: Optional[str] = Field(index=True)
    server_ids: Optional[List[str]] = Field(index=True, default=[])

