from starlette.requests import Request
import strawberry


class StrawberryHelper:
    @staticmethod
    def extract_request(info: strawberry.Info) -> Request:
        return info.context["request"]
