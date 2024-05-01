from redis_om import Field
from src.models.utility.base_redis_model import BaseRedisModel


class UserBot(BaseRedisModel):
    """Every bot has only one owner"""

    bot_id: str = Field(index=True, primary_key=True)
    user_id: str = Field(index=True)

    class Meta:  # type: ignore
        model_key_prefix = "user_bots"
