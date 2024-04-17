from typing import List
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User
from src.finders.user_finder import UserFinder
from src.resolvers.base_resolver import BaseResolver


class UsersResolver(BaseResolver):
    desc = "List of users"

    @staticmethod
    def fn() -> List[User]:
        return [UserAdapter.plug(user) for user in UserFinder.all()]
