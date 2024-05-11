import strawberry
from src.actions.bot.update_bot import UpdateBot
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
        bot = BotFinder.by_matched_user(user.pk)
        if not bot:
            raise Exception(ExceptionTypes.NO_SUCH_PAIR_FOUND)
        bot = UpdateBot.update(bot=bot, input=bot_input)
        return BotAdapter.plug(bot)
