from src.adapters.base_adapter import BaseAdapter
from src.models.bot.bot import Bot
from src.api.types.bot import Bot as BotType


class BotAdapter(BaseAdapter):
    @staticmethod
    def plug(model: Bot) -> BotType:
        if not model.pk:
            raise ValueError("No valid model is provided")
        data = {
            "id": model.id,
            "name": model.name,
            "token": model.token,
            "host": model.host,
            "port": model.port,
            "pages": model.pages,
        }
        return BotType(**data)
