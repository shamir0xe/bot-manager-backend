from typing import Optional
import strawberry


@strawberry.type
class Response:
    status: str
    message: Optional[str]

