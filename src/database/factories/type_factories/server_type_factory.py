from typing import List
from src.database.factories.base_factory import BaseFactory
from src.adapters.server_adapter import ServerAdapter
from src.database.factories.server_factory import ServerFactory
from src.api.types.server import Server as ServerType


class ServerTypeFactory(BaseFactory):
    def generate(self) -> List[ServerType]:
        return [ServerAdapter.plug(server) for server in ServerFactory().generate()]
