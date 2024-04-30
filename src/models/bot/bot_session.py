from redis_om import Field, JsonModel

from src.models.utility.base_redis_meta_class import BaseRedisMetaClass


class BotSession(JsonModel):
    user_id: str = Field(index=True)
    bot_id: str = Field(index=True)
    data: str

    class Meta(BaseRedisMetaClass):
        model_key_prefix = "bot_sessions"
