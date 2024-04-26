from redis_om import Field, JsonModel
from src.models.utility.base_redis_meta_class import BaseRedisMetaClass


class UserBot(JsonModel):
    """Every bot has only one owner"""

    bot_id: str = Field(index=True, primary_key=True)
    user_id: str = Field(index=True)

    class Meta(BaseRedisMetaClass):
        model_key_prefix = "user_bots"
