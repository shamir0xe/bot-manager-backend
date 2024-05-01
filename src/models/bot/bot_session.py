from redis_om import Field

from src.models.utility.base_redis_model import BaseRedisModel


class BotSession(BaseRedisModel):
    user_id: str = Field(index=True)
    bot_id: str = Field(index=True)
    data: str

    class Meta:  # type: ignore
        model_key_prefix = "bot_sessions"
