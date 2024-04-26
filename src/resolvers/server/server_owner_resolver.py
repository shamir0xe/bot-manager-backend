from __future__ import annotations
from typing import TYPE_CHECKING, Annotated
import strawberry
from src.finders.user_finder import UserFinder
from src.resolvers.base_resolver import BaseResolver


if TYPE_CHECKING:
    from src.api.types.server import Server as ServerType
    from src.api.types.user import User as UserType
    from src.adapters.user_adapter import UserAdapter

AnnotatedServer = Annotated["ServerType", strawberry.lazy("src.api.types.server")]
AnnotatedUser = Annotated["UserType", strawberry.lazy("src.api.types.user")]
AnnotatedUserAdapter = Annotated[
    "UserAdapter", strawberry.lazy("src.adapters.user_adapter")
]


class ServerOwnerResolver(BaseResolver[AnnotatedUser]):
    desc = "Gather the server's owner user"

    @staticmethod
    def fn(root: AnnotatedServer = strawberry.UNSET) -> AnnotatedUser:
        user_model = UserFinder.by_id(root.owner_id)
        if not user_model:
            raise Exception("No user has been found")
        return UserAdapter.plug(user_model)
