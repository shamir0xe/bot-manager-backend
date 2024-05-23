import strawberry
from actions.session.clear_session import ClearSession
from src.authorizations.handlers.session_handler import SessionHandler
from src.helpers.strawberry.strawberry_helper import StrawberryHelper
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User
from src.finders.user_finder import UserFinder
from src.resolvers.base_resolver import BaseResolver
from src.actions.user.login_user import LoginUser


class LoginResolver(BaseResolver):
    desc = "Login to the server"

    @staticmethod
    def fn(telegram_id: str = "", info: strawberry.Info = strawberry.UNSET) -> User:
        ClearSession.clear(info=info)
        user_model = LoginUser.with_telegram_id(telegram_id=telegram_id)
        return UserAdapter.plug(user_model)

        
