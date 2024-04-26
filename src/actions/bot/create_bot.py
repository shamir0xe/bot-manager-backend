from typing import Optional

from src.actions.bot.validate_bot import ValidateBot
from src.finders.bot_finder import BotFinder
from src.models.bot.bot import Bot
from src.types.exception_types import ExceptionTypes


class CreateBot:
    @staticmethod
    def create(
        id: str,
        name: str,
        token: str,
        host: Optional[str] = None,
        port: Optional[int] = None,
        pages: Optional[str] = None,
    ) -> Bot:
        bot = BotFinder.by_id(id)
        if not bot:
            bot = Bot(id=id, name=name, token=token, host=host, port=port, pages=pages)
            if not ValidateBot.validate(bot):
                raise Exception(ExceptionTypes.VALIDATOR_ERROR)
            bot.save()
        if not isinstance(bot, Bot):
            raise Exception("Cannot create the bot")
        return bot
