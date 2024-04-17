from typing import Optional

from src.helpers.types.status_types import StatusType
from src.mediators.token_mediator import TokenMediator
from src.models.user import User
from src.finders.user_finder import UserFinder


class CreateUser:
    @staticmethod
    def with_telegram_id(telegram_id: str, name: Optional[str]) -> User:
        user = UserFinder.by_telegram_id(telegram_id)
        if not user:
            if name:
                user = User(telegram_id=telegram_id, name=name)
            else:
                user = User(telegram_id=telegram_id)
            user.save()
        if not isinstance(user, User):
            raise Exception("No such user exist")
        return user
