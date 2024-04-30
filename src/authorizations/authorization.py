import functools
from typing import Dict
import strawberry
from src.finders.user_roles_finder import UserRolesFinder
from src.helpers.enums.enum_mapper import EnumMapper
from src.helpers.types.user_roles import UserRoles
from src.authorizations.handlers.bearer_token_handler import BearerTokenHandler
from src.authorizations.handlers.session_handler import SessionHandler
from src.helpers.types.authentication_types import AuthenticationTypes
from src.types.exception_types import ExceptionTypes


class Authorization:
    @staticmethod
    def auth(func=None, *, auth_type=AuthenticationTypes.BEARER):
        if func is None:
            return functools.partial(Authorization.auth, auth_type=auth_type)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            info = Authorization._get_info(kwargs)
            request = info.context["request"]
            if SessionHandler(request.session).is_authorized(
                BearerTokenHandler.extract_token(request)
            ):
                # already Authorized
                return func(*args, **kwargs)
            if auth_type is AuthenticationTypes.BEARER:
                SessionHandler(request.session).inject_dict(
                    BearerTokenHandler.with_request(request)
                )
            else:
                # TODO: other auth methods
                pass
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def _get_info(args: Dict) -> strawberry.Info:
        if "info" not in args or not isinstance(args["info"], strawberry.Info):
            raise Exception(ExceptionTypes.INVALID_ARGUMENTS)
        return args["info"]

    @staticmethod
    def role(user_role: UserRoles):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                info = Authorization._get_info(kwargs)
                request = info.context["request"]
                session_handler = SessionHandler(request.session)
                if not session_handler.is_authorized(
                    BearerTokenHandler.extract_token(request)
                ):
                    session_handler.inject_dict(
                        BearerTokenHandler.with_request(request)
                    )
                try:
                    user_roles = UserRolesFinder.with_user_id(session_handler.user_id)
                except Exception:
                    raise Exception(ExceptionTypes.NOT_PERMITTED)
                if EnumMapper.map(user_role) not in user_roles.roles:
                    raise Exception(f"You need to be a {user_role} to proceed")
                return func(*args, **kwargs)

            return wrapper

        return decorator


auth = Authorization.auth
role = Authorization.role
