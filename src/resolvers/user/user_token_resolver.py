from typing import TYPE_CHECKING, Annotated
import strawberry
from src.mediators.token_mediator import TokenMediator
from src.resolvers.base_resolver import BaseResolver

if TYPE_CHECKING:
    from src.api.types.user import User

AnnotatedUser = Annotated["User", strawberry.lazy("src.api.types.user")]


class UserTokenResolver(BaseResolver):
    desc = "Retrieve user's token if authenticated"

    @staticmethod
    def fn(root: AnnotatedUser = strawberry.UNSET) -> str:
        return TokenMediator.with_user_id(root.id).get_token()
