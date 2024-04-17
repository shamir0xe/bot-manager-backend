from typing import TYPE_CHECKING, Annotated, List

import strawberry
from src.database.factories.base_factory import BaseFactory
from src.adapters.server_adapter import ServerAdapter
from src.database.factories.server_factory import ServerFactory

if TYPE_CHECKING:
    from src.api.types.server import Server as ServerType

AnnotatedServerType = Annotated["ServerType", strawberry.lazy("src.api.types.server")]


class ServerTypeFactory(BaseFactory):
    def generate(self) -> List[AnnotatedServerType]:
        return [ServerAdapter.plug(server) for server in ServerFactory().generate()]
