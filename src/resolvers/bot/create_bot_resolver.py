import strawberry
from src.actions.bot.create_bot import CreateBot
from src.adapters.bot_adapter import BotAdapter
from src.api.types.bot import Bot as BotType
from src.helpers.types.user_roles import UserRoles
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import role


class CreateBotResolver(BaseResolver):
    desc = "Create a new bot"

    @role(UserRoles.ADMIN)
    @staticmethod
    def fn(
        id: str = strawberry.UNSET,
        name: str = strawberry.UNSET,
        token: str = strawberry.UNSET,
        info: strawberry.Info = strawberry.UNSET,
    ) -> BotType:
        bot = CreateBot.create(id=id, name=name, token=token)
        bot.save()
        return BotAdapter.plug(bot)
