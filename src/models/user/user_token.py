from datetime import datetime
from redis_om import Field, HashModel

from src.models.utility.base_redis_meta_class import BaseRedisMetaClass


class UserToken(HashModel):
    user_id: str = Field(index=True, primary_key=True)
    token: str = Field(index=True)
    expiration_date: datetime = Field(index=True)

    class Meta(BaseRedisMetaClass):
        model_key_prefix = "user_tokens"
