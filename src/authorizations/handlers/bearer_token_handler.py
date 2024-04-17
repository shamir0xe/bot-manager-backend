from typing import Any, Dict
from starlette.requests import Request

from src.mediators.token_mediator import TokenMediator


class BearerTokenHandler:
    @staticmethod
    def extract_token(request: Request) -> str:
        if not isinstance(request, Request):
            raise Exception("invalid request type")
        header_key = "Authorization"
        if header_key not in request.headers:
            raise Exception("Need to login first")
        token = request.headers.get(header_key)
        if not isinstance(token, str):
            raise Exception("Invalid token")
        return token

    @staticmethod
    def with_request(request: Request) -> Dict["str", Any]:
        data = {}
        mediator = TokenMediator.with_token(
            BearerTokenHandler.extract_token(request)
        ).check_expiration()
        if not mediator.state.is_ok:
            raise Exception("Invalid token")
        requester_id = mediator.user_id
        data["is_auth"] = "1"
        data["user_id"] = requester_id
        return data
