from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar('T')
K = TypeVar('K')

class Repository(ABC, Generic[T, K]):
    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity: T) -> T:
        pass

    @abstractmethod
    def read_by_id(self, id: K) -> T:
        pass

    @abstractmethod
    def read(self) -> List[T]:
        pass

