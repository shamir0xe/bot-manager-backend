from typing import Optional
from src.models.bot.bot_session import BotSession


class BotSessionFinder:
    @staticmethod
    def by_id(id: str) -> Optional[BotSession]:
        try:
            bot_session = BotSession.get(id)
        except Exception:
            return None
        return bot_session
