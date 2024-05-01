from typing import TYPE_CHECKING, Annotated, List
import strawberry
from src.api.types.bot_session import BotSession
from src.finders.bot_session_finder import BotSessionFinder
from src.resolvers.base_resolver import BaseResolver
from src.adapters.bot_session_adapter import BotSessionAdapter

if TYPE_CHECKING:
    from src.api.types.bot import Bot as BotType

AnnotatedBotType = Annotated["BotType", strawberry.lazy("src.api.types.bot")]


class BotSessionsResolver(BaseResolver):
    desc = "Retrieve bot sessions"

    @staticmethod
    def fn(
        root: AnnotatedBotType = strawberry.UNSET,
        info: strawberry.Info = strawberry.UNSET,
    ) -> List[BotSession]:
        bot_sessions = BotSessionFinder.bot_sessions(root.id)
        return [
            BotSessionAdapter.plug(session)
            for session in bot_sessions
        ]
