from typing import Optional
import strawberry
from src.api.types.bot_session import BotSession
from src.resolvers.bot.request_bot_session_resolver import RequestBotSessionResolver
from src.api.types.response import Response
from src.api.types.user import User
from src.api.types.bot import Bot

# from src.api.types.server import Server

from src.resolvers.bot.create_bot_resolver import CreateBotResolver
from src.resolvers.database.run_seeders_resolver import RunSeedersResolver
from src.resolvers.user.create_user_resolver import CreateUserResolver

# from src.resolvers.server.create_server_resolver import CreateServerResolver
from src.resolvers.auth.login_resolver import LoginResolver
from src.resolvers.auth.logout_resolver import LogoutResolver
from src.resolvers.bot.update_bot_resolver import UpdateBotResolver


@strawberry.type
class Mutation:
    login: Optional[User] = strawberry.field(**LoginResolver.pack())
    logout: Response = strawberry.field(**LogoutResolver.pack())
    run_seeders: Response = strawberry.field(**RunSeedersResolver.pack())

    # @role(admin)
    create_user: User = strawberry.field(**CreateUserResolver.pack())

    # @role(admin)
    create_bot: Bot = strawberry.field(**CreateBotResolver.pack())

    # @auth
    update_bot: Bot = strawberry.field(**UpdateBotResolver.pack())

    # @role(admin)
    request_bot_session: BotSession = strawberry.field(
        **RequestBotSessionResolver.pack()
    )

    # @role(admin)
    # update_bot_session: BotSession = strawberry.field(**UpdateBotSessionResolver.pack())

    # @auth @admin create_server(host, port)
    # create_server: Server = strawberry.field(**CreateServerResolver.pack())

    # @auth @admin add_subserver(server_id1, server_id2)
    # add_subserver: Server = strawberry.field(
    #     resolver=AddSubserverResolver.fn, description=AddSubServerResolver.desc
    # )
    # logout: User
