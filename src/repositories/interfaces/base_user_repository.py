from abc import ABC, abstractmethod
from src.models.user.user import User
from src.repositories.interfaces.base_repository import BaseRepository


class BaseUserRepository(BaseRepository, ABC):
    @abstractmethod
    def read_by_matched_bot(self, bot_id: str) -> User:
        pass
