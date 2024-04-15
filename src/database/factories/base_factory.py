from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Generic, List, TypeVar
from faker import Faker


T = TypeVar("T")


@dataclass
class BaseFactory(Generic[T], ABC):
    count: int = 1
    faker: Faker = field(default_factory=Faker)

    @abstractmethod
    def generate(self) -> List[T]:
        raise NotImplementedError("Subclass must override 'generate' method")

    def get_one(self, **kwargs) -> T:
        return self.generate(**kwargs)[0]
