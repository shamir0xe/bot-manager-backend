from typing import List
import strawberry

from src.adapters.user_adapter import UserAdapter
from src.finders.user_finder import UserFinder
from src.resolvers.reverse_echo import EchoResolver
from src.resolvers.users_resolver import UsersResolver
from .types.user import User


@strawberry.type
class Query:
    users: List[User] = strawberry.field(**UsersResolver.pack())
    reverse_echo: str = strawberry.field(**EchoResolver.pack())
