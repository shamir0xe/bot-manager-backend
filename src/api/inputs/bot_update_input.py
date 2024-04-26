from typing import Optional
import strawberry


@strawberry.input
class BotUpdateInput:
    name: Optional[str] = strawberry.UNSET
    token: Optional[str] = strawberry.UNSET
    pages: Optional[str] = strawberry.UNSET
    host: Optional[str] = strawberry.UNSET
    port: Optional[str] = strawberry.UNSET
