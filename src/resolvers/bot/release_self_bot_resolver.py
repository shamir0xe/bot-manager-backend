import strawberry
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User
from src.facades.auth import Auth
from src.finders.bot_finder import BotFinder
from src.models.bot.user_bot import UserBot
from src.types.exception_types import ExceptionTypes
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import auth


class ReleaseSelfBotResolver(BaseResolver):
    desc = "Release user's matched bot"

    @auth
    @staticmethod
    def fn(info: strawberry.Info = strawberry.UNSET) -> User:
        user = Auth(info).user
        if not user or not user.pk:
            raise Exception(ExceptionTypes.NO_SUCH_OBJECT_EXISTS)
        bot = BotFinder.by_matched_user(user.pk)
        if bot:
            user_bots = UserBot.find(
                (UserBot.user_id == user.pk) & (UserBot.bot_id == bot.id)
            ).all()
            try:
                UserBot.delete_many(user_bots)
            except Exception:
                pass
        return UserAdapter.plug(user)
