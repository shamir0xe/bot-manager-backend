import strawberry
from src.actions.session.clear_session import ClearSession
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User
from src.resolvers.base_resolver import BaseResolver
from src.actions.user.login_user import LoginUser


class LoginResolver(BaseResolver):
    desc = "Login or register the user"

    @staticmethod
    def fn(telegram_id: str = "", info: strawberry.Info = strawberry.UNSET) -> User:
        ClearSession.clear(info=info)
        user_model = LoginUser.login_or_register(telegram_id=telegram_id)
        return UserAdapter.plug(user_model)
