from typing import List, TYPE_CHECKING, Annotated
import strawberry

from src.finders.server_finder import ServerFinder
from src.adapters.server_adapter import ServerAdapter
from src.resolvers.base_resolver import BaseResolver
from src.api.types.server import Server as ServerType
from src.models.server import Server


if TYPE_CHECKING:
    from src.api.types.user import User as UserType

AnnotatedUserType = Annotated["UserType", strawberry.lazy("src.api.types.user")]
# AnnotatedServerType = Annotated["Server", strawberry.lazy("src.api.types.server")]


class UserServersResolver(BaseResolver[List[ServerType]]):
    desc = "servers of the user"

    @staticmethod
    def fn(
        root: AnnotatedUserType = strawberry.UNSET
    ) -> List[ServerType]:
        server_list: List[ServerType] = []
        for server in ServerFinder.by_ids(root.server_ids):
            server_list += [ServerAdapter.plug(server)]
        return server_list
