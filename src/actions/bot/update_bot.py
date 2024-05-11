from src.actions.bot.validate_bot import ValidateBot
from src.api.inputs.bot_update_input import BotUpdateInput
from src.models.bot.bot import Bot
from src.types.exception_types import ExceptionTypes


class UpdateBot:
    @staticmethod
    def update(bot: Bot, input: BotUpdateInput) -> Bot:
        if input.name:
            bot.name = input.name
        if input.token:
            bot.token = input.token
        if input.pages:
            bot.pages = input.pages
        if input.host:
            bot.host = input.host
        if input.port:
            bot.host = input.host
        if not ValidateBot.validate(bot):
            raise Exception(ExceptionTypes.VALIDATOR_ERROR)
        bot.save()
        return bot
