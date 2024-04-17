from typing import Optional
import strawberry
from src.api.types.response import Response
from src.resolvers.run_seeders_resolver import RunSeedersResolver
from src.api.types.user import User

from src.api.types.server import Server
from src.resolvers.create_user_resolver import CreateUserResolver

# from src.resolvers.create_server_resolver import CreateServerResolver
from src.resolvers.login_resolver import LoginResolver
from src.resolvers.logout_resolver import LogoutResolver


@strawberry.type
class Mutation:
    login: Optional[User] = strawberry.field(**LoginResolver.pack())
    logout: Response = strawberry.field(**LogoutResolver.pack())
    run_seeders: Response = strawberry.field(**RunSeedersResolver.pack())

    # @auth @role(admin)
    create_user: User = strawberry.field(**CreateUserResolver.pack())

    # @auth @admin create_server(host, port)
    # create_server: Server = strawberry.field(**CreateServerResolver.pack())

    # @auth @admin add_subserver(server_id1, server_id2)
    # add_subserver: Server = strawberry.field(
    #     resolver=AddSubserverResolver.fn, description=AddSubServerResolver.desc
    # )
    # logout: User
