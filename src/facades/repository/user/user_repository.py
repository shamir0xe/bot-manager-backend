from typing import List
from src.repositories.interfaces.base_user_repository import BaseUserRepository
from src.facades.env import Env
from src.helpers.decorators.singleton import singleton
from src.models.user.user import User
from src.repositories.local.user.user_local_repository import UserLocalRepository
from src.types.exception_types import ExceptionTypes
from src.types.repository_types import RepositoryTypes


@singleton
class UserRepository(BaseUserRepository):
    def __init__(self) -> None:
        if Env().repository == RepositoryTypes.LOCAL:
            self.instance = UserLocalRepository()
        else:
            raise Exception(ExceptionTypes.REPOSITORY_NOT_SUPPORTED)

    def read(self) -> List[User]:
        return self.instance.read()

    def read_by_matched_bot(self, bot_id: str) -> User:
        return self.instance.read_by_matched_bot(bot_id)

    def read_by_id(self, id: str) -> User:
        return self.instance.read_by_id(id)

    def create(self, entity: User) -> User:
        return self.instance.create(entity)

    def delete(self, entity: User) -> User:
        return self.instance.delete(entity)

    def update(self, entity: User) -> User:
        return self.instance.update(entity)
