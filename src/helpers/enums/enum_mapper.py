from enum import Enum


class EnumMapper:
    @staticmethod
    def map(e: Enum) -> str:
        return e.name.lower()
