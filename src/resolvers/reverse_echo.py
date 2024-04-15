import strawberry
from src.resolvers.base_resolver import BaseResolver


class ReverseEcho(BaseResolver[str]):
    desc = "just reverse echoing everything you say xD"

    @staticmethod
    def fn(sentence: str = "") -> str:
        return "".join(sentence[(-1) * (i + 1)] for i in range(len(sentence)))
