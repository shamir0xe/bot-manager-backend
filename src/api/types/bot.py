from typing import List, Optional
import strawberry

from src.resolvers.bot.bot_sessions_resolver import BotSessionsResolver
from src.api.types.bot_session import BotSession
from src.api.types.user import User
from src.resolvers.bot.bot_owner_resolver import BotOwnerResolver


@strawberry.type
class Bot:
    id: str
    name: str
    token: str
    host: Optional[str]
    port: Optional[int]
    pages: Optional[str]

    ## A bot can have at most 1 owner
    owner: Optional[User] = strawberry.field(**BotOwnerResolver.pack())

    ## bot sessions
    sessions: List[BotSession] = strawberry.field(**BotSessionsResolver.pack())
