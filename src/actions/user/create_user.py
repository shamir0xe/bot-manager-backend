from typing import Optional

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
        return user
