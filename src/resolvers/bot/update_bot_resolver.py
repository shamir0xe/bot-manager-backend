import strawberry
from src.actions.bot.validate_bot import ValidateBot
from src.adapters.bot_adapter import BotAdapter
from src.api.inputs.bot_update_input import BotUpdateInput
from src.api.types.bot import Bot
from src.facades.auth import Auth
from src.finders.bot_finder import BotFinder
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import auth
from src.types.exception_types import ExceptionTypes


class UpdateBotResolver(BaseResolver):
    desc = "Update user's bot information"

    @auth
    @staticmethod
    def fn(
        bot_input: BotUpdateInput = strawberry.UNSET,
        info: strawberry.Info = strawberry.UNSET,
    ) -> Bot:
        user = Auth(info).user
        if not user or not user.pk:
            raise Exception(ExceptionTypes.LOGIN_NEEDED)
        bot = BotFinder.by_matched_user(user.pk)
        if not bot:
            raise Exception(ExceptionTypes.NO_SUCH_PAIR_FOUND)
        if bot_input.name:
            bot.name = bot_input.name
        if bot_input.token:
            bot.token = bot_input.token
        if bot_input.pages:
            bot.pages = bot_input.pages
        if bot_input.host:
            bot.host = bot_input.host
        if bot_input.port:
            bot.host = bot_input.host
        if not ValidateBot.validate(bot):
            raise Exception(ExceptionTypes.VALIDATOR_ERROR)
        bot.save()
        return BotAdapter.plug(bot)
