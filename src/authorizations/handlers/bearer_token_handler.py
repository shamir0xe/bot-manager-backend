from typing import Any, Dict
from starlette.requests import Request

from src.mediators.token_mediator import TokenMediator
from src.types.exception_types import ExceptionTypes


class BearerTokenHandler:
    @staticmethod
    def extract_token(request: Request) -> str:
        if not isinstance(request, Request):
            raise Exception(ExceptionTypes.INVALID_REQUEST)
        header_key = "Authorization"
        if header_key not in request.headers:
            raise Exception(ExceptionTypes.LOGIN_NEEDED)
        token = request.headers.get(header_key)
        if not isinstance(token, str):
            raise Exception(ExceptionTypes.INVALID_TOKEN)
        return token

    @staticmethod
    def with_request(request: Request) -> Dict["str", Any]:
        data = {}
        mediator = TokenMediator.with_token(
            BearerTokenHandler.extract_token(request)
        ).check_expiration()
        if not mediator.state.is_ok:
            raise Exception(ExceptionTypes.INVALID_TOKEN)
        requester_id = mediator.user_id
        data["is_auth"] = "1"
        data["user_id"] = requester_id
        return data
