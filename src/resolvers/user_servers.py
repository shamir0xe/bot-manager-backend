from typing import List, TYPE_CHECKING, Annotated
import strawberry

from src.resolvers.base_resolver import BaseResolver


if TYPE_CHECKING:
    from src.api.types.user import User
    from src.api.types.server import Server

user_type = Annotated["User", strawberry.lazy("src.api.types.user")]
server_type = Annotated["Server", strawberry.lazy("src.api.types.server")]


class UserServers(BaseResolver):
    desc = "servers of the user"

    @staticmethod
    def fn(root: user_type, info: strawberry.Info) -> List[server_type]:
        return []
