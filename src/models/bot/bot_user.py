from src.models.utility.base_redis_model import BaseRedisModel


class BotUser(BaseRedisModel):
    """Every bot has only one owner"""

    bot_id: str # pk
    user_id: str
