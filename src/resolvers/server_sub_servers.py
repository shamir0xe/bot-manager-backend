from typing import List, TYPE_CHECKING, Annotated
import strawberry

from src.database.factories.server_factory import ServerFactory
from src.adapters.server_adapter import ServerAdapter
from src.resolvers.base_resolver import BaseResolver
from src.models.server import Server as ServerModel

if TYPE_CHECKING:
    from src.api.types.server import Server as ServerType


AnnotatedServerType = Annotated["ServerType", strawberry.lazy("src.api.types.server")]


class ServerSubServers(BaseResolver[List[AnnotatedServerType]]):
    desc = "subservers of the servers"

    @staticmethod
    def fn(
        server: AnnotatedServerType = DummyFactory.ServerType()),
    ) -> List[AnnotatedServerType]:
        servers = []
        try:
            data = ServerModel.find(ServerModel.pk == server.id).all()
            for server_model in data:
                if isinstance(server_model, ServerModel):
                    servers += [ServerAdapter.plug(server_model)]
        except Exception:
            # TODO
            pass
        return servers
