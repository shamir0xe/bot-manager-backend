from src.models.bot.user_bot import UserBot


class MatchBotUser:
    @staticmethod
    def match(bot_id: str, user_id: str) -> bool:
        try:
            pair = UserBot(bot_id=bot_id, user_id=user_id)
            pair.save()
        except Exception as e:
            print(f"Exception: {e}")
            return False
        return True
