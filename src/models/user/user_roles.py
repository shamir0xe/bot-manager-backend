from typing import List
from redis_om import Field, JsonModel

from src.models.utility.base_redis_meta_class import BaseRedisMetaClass


class UserRoles(JsonModel):
    user_id: str = Field(index=True, primary_key=True)
    roles: List[str] = Field(index=True)

    class Meta(BaseRedisMetaClass):
        model_key_prefix = "user_roles"
