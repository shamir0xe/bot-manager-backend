import strawberry
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
        SessionHandler(StrawberryHelper.extract_request(info).session).clear_session()
        user_model = UserFinder.by_telegram_id(telegram_id)
        if not user_model:
            raise Exception("No user with this telegram_id is found")
        user = UserAdapter.plug(user_model)
        LoginUser.with_user_id(user.id)
        return user
