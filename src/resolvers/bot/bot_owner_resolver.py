from typing import TYPE_CHECKING, Annotated
import strawberry
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User
from src.finders.user_finder import UserFinder
from src.resolvers.base_resolver import BaseResolver
from src.types.exception_types import ExceptionTypes

if TYPE_CHECKING:
    from src.api.types.bot import Bot as BotType

AnnotatedBotType = Annotated["BotType", strawberry.lazy("src.api.types.bot")]


class BotOwnerResolver(BaseResolver):
    desc = "Return owner user of the bot"

    @staticmethod
    def fn(
        root: AnnotatedBotType = strawberry.UNSET,
        info: strawberry.Info = strawberry.UNSET,
    ) -> User:
        bot_id = root.id
        user = UserFinder.by_matched_bot(bot_id=bot_id)
        if not user:
            raise Exception(ExceptionTypes.NO_SUCH_PAIR_FOUND)
        return UserAdapter.plug(user)
