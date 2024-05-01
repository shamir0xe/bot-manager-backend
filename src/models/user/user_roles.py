from typing import List
from redis_om import Field
from src.models.utility.base_redis_model import BaseRedisModel


class UserRoles(BaseRedisModel):
    user_id: str = Field(index=True, primary_key=True)
    roles: List[str] = Field(index=True)

    class Meta:  # type: ignore
        model_key_prefix = "user_roles"
