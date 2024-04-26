from typing import List, Optional
from src.models.server.server import Server


class ServerFinder:
    @staticmethod
    def by_address(address: str) -> Optional[Server]:
        try:
            server = Server.find(Server.address == address).first()
            if isinstance(server, Server):
                return server
        except Exception as e:
            print(f"error occured in serverfinder: {e}")
        return None

    @staticmethod
    def by_ids(ids: List[str]) -> List[Server]:
        servers: List[Server] = []
        if not ids:
            return servers
        try:
            for server in Server.find(Server.pk << ids).all():  # type: ignore
                if isinstance(server, Server):
                    servers += [server]
        except Exception as e:
            print(f"error occured in serverfinder: {e}")
        return servers
