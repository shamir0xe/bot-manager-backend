from typing import Optional
from redis_om import Migrator, NotFoundError
from src.models.bot.bot import Bot
from src.models.bot.user_bot import UserBot
from src.types.exception_types import ExceptionTypes


class BotFinder:
    @staticmethod
    def by_id(id: str) -> Optional[Bot]:
        try:
            return Bot.get(id)
        except NotFoundError:
            return None

    @staticmethod
    def by_matched_user(user_id: str) -> Optional[Bot]:
        # Migrator().run()
        user_bot = None
        try:
            user_bot = UserBot.find(UserBot.user_id == user_id).first()
        except Exception:
            pass
        if not isinstance(user_bot, UserBot):
            return None
        return BotFinder.by_id(user_bot.bot_id)

    @staticmethod
    def free_bot() -> Optional[Bot]:
        for bot_id in Bot.all_pks():
            user_bot = None
            try:
                user_bot = UserBot.find(UserBot.bot_id == bot_id).first()
            except Exception:
                pass
            if not user_bot:
                ## we don't have any pair for this bot
                return BotFinder.by_id(bot_id)
        return None
