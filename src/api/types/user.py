from __future__ import annotations
from typing import List, Optional
import strawberry
from src.resolvers.user_servers import UserServers
from .server import Server


@strawberry.type
class User:
    server_ids: strawberry.Private[List[str]]

    id: str
    telegram_id: str
    name: Optional[str]
    servers: List[Server] = strawberry.field(
        resolver=UserServers.fn, description=UserServers.desc
    )

