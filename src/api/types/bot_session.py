import strawberry
from src.api.types.user import User


@strawberry.type
class BotSession:
    id: str
    user: User
    data: str
