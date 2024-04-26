from __future__ import annotations
from typing import List, Optional
import strawberry
from src.resolvers.user.user_servers_resolver import UserServersResolver
from src.resolvers.user.user_token_resolver import UserTokenResolver
from .server import Server


@strawberry.type
class User:
    server_ids: strawberry.Private[List[str]]

    id: str
    telegram_id: str
    name: Optional[str]
    # servers()
    servers: List[Server] = strawberry.field(**UserServersResolver.pack())
    # token, if logged in
    token: Optional[str] = strawberry.field(**UserTokenResolver.pack())
