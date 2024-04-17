from typing import List, Optional
from redis_om import NotFoundError
from src.models.user import User


class UserFinder:
    @staticmethod
    def by_id(id: str) -> Optional[User]:
        try:
            return User.get(id)
        except NotFoundError:
            return None

    @staticmethod
    def by_telegram_id(telegram_id: str) -> Optional[User]:
        try:
            user = User.find(User.telegram_id == telegram_id).first()
            if isinstance(user, User):
                return user
            return None
        except NotFoundError:
            return None

    @staticmethod
    def all() -> List[User]:
        try:
            return [User.get(id) for id in User.all_pks()]
        except Exception as e:
            print(e)
            return []
