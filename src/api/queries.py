from typing import List
import strawberry

from src.resolvers.bot.bot_info_resolver import BotInfoResolver
from src.api.types.bot import Bot
from src.resolvers.utility.reverse_echo import EchoResolver
from src.resolvers.user.users_resolver import UsersResolver
from src.resolvers.bot.request_bot_resolver import RequestBotResolver
from .types.user import User


@strawberry.type
class Query:
    users: List[User] = strawberry.field(**UsersResolver.pack())
    reverse_echo: str = strawberry.field(**EchoResolver.pack())

    # @auth
    reqeust_bot: Bot = strawberry.field(**RequestBotResolver.pack())

    # @admin
    bot_info: Bot = strawberry.field(**BotInfoResolver.pack())

    # @auth
    # get_file: File = strawberry.field(**GetFileResolver.pack())
