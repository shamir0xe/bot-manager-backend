from typing import List

import strawberry
from src.helpers.types.user_roles import UserRoles
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User
from src.finders.user_finder import UserFinder
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import role


class UsersResolver(BaseResolver):
    desc = "List of users"

    @role(UserRoles.ADMIN)
    @staticmethod
    def fn(info: strawberry.Info = strawberry.UNSET) -> List[User]:
        return [UserAdapter.plug(user) for user in UserFinder.all()]
