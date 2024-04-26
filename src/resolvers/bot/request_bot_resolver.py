import strawberry
from src.actions.bot.match_bot_user import MatchBotUser
from src.adapters.bot_adapter import BotAdapter
from src.api.types.bot import Bot
from src.facades.auth import Auth
from src.finders.bot_finder import BotFinder
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import auth
from src.types.exception_types import ExceptionTypes


class RequestBotResolver(BaseResolver):
    desc = "Requesting a bot (maybe new) from the server"

    @auth
    @staticmethod
    def fn(info: strawberry.Info = strawberry.UNSET) -> Bot:
        user = Auth(info).user
        if not user or not user.pk:
            raise Exception(ExceptionTypes.LOGIN_NEEDED)
        bot = BotFinder.by_matched_user(user.pk)
        if bot:
            ## already have a bot
            return BotAdapter.plug(bot)
        bot = BotFinder.free_bot()
        if bot and bot.pk:
            res = MatchBotUser.match(bot.id, user.pk)
            if not res:
                raise Exception(ExceptionTypes.CANNOT_CREATE_PAIR)
            return BotAdapter.plug(bot)
        raise Exception(ExceptionTypes.NO_BOT_AVAILABLE)
