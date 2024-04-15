from typing import TypeVar, Generic
from abc import ABC, abstractmethod

# Define type variables for model and type
M = TypeVar("M")  # Represents the model type
T = TypeVar("T")  # Represents the target type


class BaseAdapter(Generic[M, T], ABC):
    @staticmethod
    @abstractmethod
    def plug(model: M) -> T:
        """
        Convert a model instance to the target type.

        Args:
            model: The model instance to be converted.

        Returns:
            An instance of the target type.
        """
        pass
