from abc import ABC, abstractmethod
from src.models.user.user_token import UserToken
from src.repositories.interfaces.base_repository import BaseRepository


class BaseUserTokenRepository(BaseRepository, ABC):
    @abstractmethod
    def read_by_token(self, token: str) -> UserToken:
        pass
