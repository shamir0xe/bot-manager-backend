from typing import List
from redis_om import NotFoundError
from src.models.user import User


class UserFinder:
    @staticmethod
    def by_id(id: str) -> User | None:
        try:
            return User.get(id)
        except NotFoundError:
            return None

    @staticmethod
    def by_telegram_id(telegram_id: str) -> User | None:
        try:
            return User.get(telegram_id)
        except NotFoundError:
            return None

    @staticmethod
    def all() -> List[User]:
        try:
            users = User.find().all()
            all_users = []
            for user in users:
                all_users += [user]
            return all_users
        except Exception:
            return []
