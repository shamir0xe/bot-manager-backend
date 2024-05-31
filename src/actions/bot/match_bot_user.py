from typing import Optional
from src.models.bot.user_bot import BotUser


class MatchBotUser:
    @staticmethod
    def match(bot_id: str, user_id: Optional[str]) -> bool:
        try:
            pair = BotUser(bot_id=bot_id, user_id=user_id)
            pair.save()
        except Exception as e:
            print(f"Exception: {e}")
            return False
        return True
