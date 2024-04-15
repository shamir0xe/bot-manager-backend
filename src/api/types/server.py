from __future__ import annotations
from typing import List
import strawberry
from src.resolvers.server_sub_servers import ServerSubServers


@strawberry.type
class Server:
    server_ids: strawberry.Private[List[str]]

    id: str
    address: str
    port: int
    sub_servers: List[Server] = strawberry.field(
        resolver=ServerSubServers.fn, description=ServerSubServers.desc
    )
