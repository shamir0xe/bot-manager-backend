from datetime import datetime
from redis_om import Field
from src.models.utility.base_redis_model import BaseRedisModel


class UserToken(BaseRedisModel):
    user_id: str = Field(index=True, primary_key=True)
    token: str = Field(index=True)
    expiration_date: datetime = Field(index=True)

    class Meta:  # type: ignore
        model_key_prefix = "user_tokens"
