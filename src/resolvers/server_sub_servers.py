from typing import List, TYPE_CHECKING, Annotated, Union
import strawberry

from src.adapters.server_adapter import ServerAdapter
from src.resolvers.base_resolver import BaseResolver
from src.models.server import Server as ServerModel

if TYPE_CHECKING:
    from src.api.types.server import Server


AnnotatedServerType = Annotated["Server", strawberry.lazy("src.api.types.server")]


class ServerSubServers(BaseResolver[List[AnnotatedServerType]]):
    desc = "subservers of the servers"

    @staticmethod
    def fn(
        root: AnnotatedServerType = strawberry.UNSET,
    ) -> List[AnnotatedServerType]:
        servers = []
        try:
            if root is strawberry.UNSET:
                raise Exception("No valid server provided")
            data = ServerModel.find(ServerModel.pk == root.id).all()
            for server_model in data:
                if isinstance(server_model, ServerModel):
                    servers += [ServerAdapter.plug(server_model)]
        except Exception:
            # TODO
            pass
        return servers
