import strawberry
from src.adapters.bot_adapter import BotAdapter
from src.api.types.bot import Bot
from src.finders.bot_finder import BotFinder
from src.helpers.types.user_roles import UserRoles
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import role
from src.types.exception_types import ExceptionTypes


class BotInfoResolver(BaseResolver):
    desc = "Bot info fetcher, [admin]"

    @role(UserRoles.ADMIN)
    @staticmethod
    def fn(
        bot_id: str = strawberry.UNSET, info: strawberry.Info = strawberry.UNSET
    ) -> Bot:
        bot = BotFinder.by_id(bot_id)
        if not bot:
            raise Exception(ExceptionTypes.NO_SUCH_OBJECT_EXISTS)
        return BotAdapter.plug(bot)
