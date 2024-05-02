import strawberry
from src.api.types.bot import Bot
from src.finders.bot_finder import BotFinder
from src.finders.user_finder import UserFinder
from src.helpers.types.user_roles import UserRoles
from src.models.bot.user_bot import UserBot
from src.adapters.bot_adapter import BotAdapter
from src.types.exception_types import ExceptionTypes
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import role


class ReleaseBotResolver(BaseResolver):
    desc = "Release bot from it's current owner"

    @role(UserRoles.ADMIN)
    @staticmethod
    def fn(
        bot_id: str = strawberry.UNSET, info: strawberry.Info = strawberry.UNSET
    ) -> Bot:
        bot = BotFinder.by_id(bot_id)
        if not bot:
            raise Exception(ExceptionTypes.NO_SUCH_OBJECT_EXISTS)
        user = UserFinder.by_matched_bot(bot_id)
        if user:
            # we're gonna remove the connection
            user_bots = UserBot.find(
                (UserBot.user_id == user.pk) & (UserBot.bot_id == bot_id)
            ).all()
            try:
                UserBot.delete_many(user_bots)
            except Exception:
                pass
        return BotAdapter.plug(bot)
