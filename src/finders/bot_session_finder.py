from typing import List, Optional
from src.models.bot.bot_session import BotSession


class BotSessionFinder:
    @staticmethod
    def by_id(id: str) -> Optional[BotSession]:
        try:
            bot_session = BotSession.get(id)
        except Exception:
            return None
        return bot_session

    @staticmethod
    def bot_sessions(bot_id: str) -> List[BotSession]:
        sessions = []
        try:
            sessions = BotSession.find(BotSession.bot_id == bot_id).all()
        except Exception:
            return []
        result = []
        for session in sessions:
            if isinstance(session, BotSession):
                result += [session]
        return result
