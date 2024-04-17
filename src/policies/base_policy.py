from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar


T = TypeVar("T")  # Represents the target type


class BasePolicy(Generic[T], ABC):
    role: Optional[str] = None

    def __init_subclass__(cls) -> None:
        if not cls.role:
            raise NotImplementedError("Subclass must override 'role' attribute")


    @staticmethod
    @abstractmethod
    def check() -> T:
        raise NotImplementedError("Subclass must override 'check' method")

