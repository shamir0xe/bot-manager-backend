from src.adapters.base_adapter import BaseAdapter
from src.models.bot.bot import Bot
from src.models.local_repository.bot.alch_bot import AlchBot


class AlchBotAdapter(BaseAdapter):
    @staticmethod
    def plug(model: AlchBot) -> Bot:
        return Bot(
            id=model.id,
            name=model.name,
            token=model.token,
            host=model.host,
            port=model.port,
            pages=model.pages,
        )
