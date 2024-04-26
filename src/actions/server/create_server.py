from typing import Optional
from pydantic import PositiveInt

from src.models.server.server import Server
from src.finders.server_finder import ServerFinder


class CreateServer:
    @staticmethod
    def with_address(address: str, port: Optional[PositiveInt]) -> Server:
        server = ServerFinder.by_address(address)
        if not server:
            if port:
                server = Server(address=address, port=port)
            else:
                server = Server(address)
            server.save()
        return server


