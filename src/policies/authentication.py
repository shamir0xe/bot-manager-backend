from typing import Any, Optional

# from blacksheep import Application, Request, auth, get, json
# from guardpost import AuthenticationHandler, Identity
import strawberry

from src.helpers.state_manager import State
from src.adapters.user_adapter import UserAdapter
from src.finders.user_finder import UserFinder
from src.helpers.mappers.authentication_mapper import AuthenticationMapper
from src.helpers.types.authentication_types import AuthenticationTypes
from src.mediators.token_mediator import TokenMediator


# class GuardAuthHandler(AuthenticationHandler):
#     def authenticate(self, context: Request) -> Optional[Identity]:
#         print(context)
#         header_value = context.get_first_header(b"Authentication")
#         context.identity = None
#         print("in the auth 'guard' handler")
#         if isinstance(header_value, str):
#             token_mediator = TokenMediator.with_token(header_value)
#             if not token_mediator.state.is_ok:
#                 # not a valid token
#                 return context.identity
#             user_model = UserFinder.by_id(token_mediator.user_id)
#             if not user_model:
#                 return context.identity
#             user = UserAdapter.plug(user_model)
#             context.identity = Identity(
#                 {"telegram_id": user.telegram_id},
#                 AuthenticationMapper.map(AuthenticationTypes.GUARD),
#             )
#         return context.identity

from starlette.requests import Request


class Authentication:
    # @staticmethod
    # def with_user_id(info: Any) -> State:
    #     header_value = info.context['request']
    #     from starlette.requests import Request as RQ
    #     debug_text(info.context)
    #     debug_text("Authentication" in info.context['request'].headers)
    #     RQ.headers
    #     debug_text(info.root_value)
    #     return State.ok()

    @staticmethod
    def auth(info: strawberry.Info) -> State:
        request: Request = info.context["request"]
        auth_key = "Authorization"
        if auth_key in request.headers:
            token = request.headers.get(auth_key)
            if not isinstance(token, str):
                return State.failure("No token provided")
            mediator = TokenMediator.with_token(token).check_expiration()
            if not mediator.state.is_ok:
                return mediator.state
            # giving user_id back to the function as a result
            return State.ok(mediator.user_id)
        return State.failure("No token provided")
