from typing import Any
from pylib_0xe.config.config import Config as Cfg


class Config:
    @staticmethod
    def read(selector: str) -> Any:
        return Cfg(__file__).read(selector)
