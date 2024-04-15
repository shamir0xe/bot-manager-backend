from typing import Optional

from redis_om import NotFoundError
from src.models.server import Server


class ServerFinder:
    @staticmethod
    def by_address(address: str) -> Optional[Server]:
        try:
            server = Server.find(Server.address == address).first()
            if isinstance(server, Server):
                return server
            return None
        except NotFoundError:
            return None
