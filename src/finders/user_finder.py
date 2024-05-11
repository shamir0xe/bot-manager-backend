from typing import List, Optional
from redis_om import NotFoundError
from src.models.bot.user_bot import UserBot
from src.models.user.user import User


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

    @staticmethod
    def by_matched_bot(bot_id: str) -> Optional[User]:
        """Find and return the user mathed to the bot_id"""
        # Migrator().run()
        user_bot = None
        try:
            user_bot = UserBot.find(UserBot.bot_id == bot_id).first()
        except Exception:
            pass
        if not user_bot:
            return None
        return UserFinder.by_id(user_bot.user_id)
