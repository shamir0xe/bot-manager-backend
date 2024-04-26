import strawberry
from src.helpers.types.user_roles import UserRoles
from src.actions.user.create_user import CreateUser
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User as UserType
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import role


class CreateUserResolver(BaseResolver):
    desc = "creating a new user, [dev] scope"

    @role(UserRoles.ADMIN)
    @staticmethod
    def fn(
        telegram_id: str = strawberry.UNSET,
        name: str = strawberry.UNSET,
        info: strawberry.Info = strawberry.UNSET,
    ) -> UserType:
        user = CreateUser.with_telegram_id(telegram_id=telegram_id, name=name)
        user.save()
        return UserAdapter.plug(user)
