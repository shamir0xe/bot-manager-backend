from typing import List
import strawberry

from src.adapters.user_adapter import UserAdapter
from src.finders.user_finder import UserFinder
from src.resolvers.reverse_echo import ReverseEcho
from .types.user import User


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        return [UserAdapter.plug(user) for user in UserFinder.all()]

    reverse_echo: str = strawberry.field(
        resolver=ReverseEcho.fn,
        description=ReverseEcho.desc,
    )
