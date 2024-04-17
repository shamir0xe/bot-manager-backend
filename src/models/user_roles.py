from typing import List
from redis_om import Field, JsonModel


class UserRoles(JsonModel):
    user_id: str = Field(index=True, primary_key=True)
    roles: List[str] = Field(index=True)
