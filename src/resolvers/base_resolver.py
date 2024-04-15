from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar


T = TypeVar("T")  # Represents the target type


class BaseResolver(Generic[T], ABC):
    desc: Optional[str] = None

    def __init_subclass__(cls) -> None:
        if not cls.desc:
            raise NotImplementedError("Subclass must override 'desc' attribute")

    @staticmethod
    @abstractmethod
    def fn() -> T:
        raise NotImplementedError("Subclass must override 'fn' method")
