import strawberry
from src.adapters.bot_session_adapter import BotSessionAdapter
from src.api.types.bot_session import BotSession
from src.finders.bot_session_finder import BotSessionFinder
from src.helpers.types.user_roles import UserRoles
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import role
from src.types.exception_types import ExceptionTypes


class UpdateBotSessionResolver(BaseResolver):
    desc = "Update bot session data"

    @role(UserRoles.ADMIN)
    @staticmethod
    def fn(
        session_id: str = strawberry.UNSET,
        data: str = strawberry.UNSET,
        info: strawberry.Info = strawberry.UNSET,
    ) -> BotSession:
        bot_session = BotSessionFinder.by_id(session_id)
        if not bot_session:
            raise Exception(ExceptionTypes.NO_SUCH_OBJECT_EXISTS)
        bot_session.data = data
        bot_session.save()
        return BotSessionAdapter.plug(bot_session)
