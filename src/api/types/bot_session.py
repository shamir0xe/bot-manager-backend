import strawberry

from src.api.types.bot import Bot
from src.api.types.user import User


@strawberry.type
class BotSession:
    id: str
    bot: Bot
    user: User
    data: str
