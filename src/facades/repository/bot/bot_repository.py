from typing import List
from models.bot.bot import Bot
from repositories.interfaces.base_bot_repository import BaseBotRepository
from src.facades.env import Env
from src.helpers.decorators.singleton import singleton
from src.types.exception_types import ExceptionTypes
from src.types.repository_types import RepositoryTypes


@singleton
class BotRepository(BaseBotRepository):
    def __init__(self) -> None:
        if Env().repository == RepositoryTypes.LOCAL:
            self.instance = BotLocalRepository()
        else:
            raise Exception(ExceptionTypes.REPOSITORY_NOT_SUPPORTED)

    def read(self) -> List[Bot]:
        return self.instance.read()

    def read_by_id(self, id: str) -> Bot:
        return self.instance.read_by_id(id)

    def create(self, entity: Bot) -> Bot:
        return self.instance.create(entity)

    def delete(self, entity: Bot) -> Bot:
        return self.instance.delete(entity)

    def update(self, entity: Bot) -> Bot:
        return self.instance.update(entity)
