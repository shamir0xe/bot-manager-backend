from src.models.bot.bot import Bot
from src.validators.bot.bot_validator import BotValidator


class ValidateBot:
    @staticmethod
    def validate(bot: Bot) -> bool:
        try:
            BotValidator(**bot.dict())
        except Exception as e:
            print(f"Exception {str(e)}")
            return False
        return True
