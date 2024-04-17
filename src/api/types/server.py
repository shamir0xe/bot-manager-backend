from typing import TYPE_CHECKING, Annotated, List
import strawberry
from src.resolvers.server_sub_servers import ServerSubServers
from src.resolvers.server_owner_resolver import ServerOwnerResolver

if TYPE_CHECKING:
    from src.api.types.user import User

AnnotatedUser = Annotated["User", strawberry.lazy("src.api.types.user")]


@strawberry.type
class Server:
    server_ids: strawberry.Private[List[str]]
    owner_id: strawberry.Private[str]

    id: str
    address: str
    port: int
    owner: AnnotatedUser = strawberry.field(**ServerOwnerResolver.pack())
    sub_servers: List["Server"] = strawberry.field(**ServerSubServers.pack())
