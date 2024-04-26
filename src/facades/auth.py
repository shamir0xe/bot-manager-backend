import strawberry
from dataclasses import dataclass
from typing import Optional
from src.authorizations.handlers.session_handler import SessionHandler
from src.finders.user_finder import UserFinder
from src.models.user.user import User


@dataclass
class Auth:
    info: strawberry.Info

    @property
    def user(self) -> Optional[User]:
        if not isinstance(self.info, strawberry.Info):
            return None
        request = self.info.context["request"]
        user_id = SessionHandler(request.session).user_id
        return UserFinder.by_id(user_id)
