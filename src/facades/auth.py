import strawberry
from dataclasses import dataclass
from src.authorizations.handlers.session_handler import SessionHandler
from src.finders.user_finder import UserFinder
from src.models.user.user import User
from src.types.exception_types import ExceptionTypes


@dataclass
class Auth:
    info: strawberry.Info

    @property
    def user(self) -> User:
        if not isinstance(self.info, strawberry.Info):
            # invalid args from the resolver
            raise Exception(ExceptionTypes.INVALID_ARGUMENTS)
        request = self.info.context["request"]
        user_id = SessionHandler(request.session).user_id
        user = UserFinder.by_id(user_id)
        if not user or not user.pk:
            # not logged in
            raise Exception(ExceptionTypes.LOGIN_NEEDED)
        return user
