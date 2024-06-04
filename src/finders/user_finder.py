from typing import List, Optional
from src.facades.repository.user.user_repository import UserRepository
from src.models.user.user import User


class UserFinder:
    @staticmethod
    def by_telegram_id(telegram_id: str) -> Optional[User]:
        user = UserRepository().read_by_id(id=telegram_id)
        if not isinstance(user, User):
            return None
        return user

    @staticmethod
    def all() -> List[User]:
        return UserRepository().read()

    @staticmethod
    def by_matched_bot(bot_id: str) -> Optional[User]:
        """Find and return the user mathed to the bot_id"""
        return UserRepository().read_by_matched_bot(bot_id)
