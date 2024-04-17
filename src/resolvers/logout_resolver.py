import strawberry
from src.api.types.response import Response
from src.authorizations.handlers.session_handler import SessionHandler
from src.helpers.state_manager import State
from src.helpers.strawberry.strawberry_helper import StrawberryHelper
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import auth


class LogoutResolver(BaseResolver):
    desc = "Logout from the server"

    @auth
    @staticmethod
    def fn(info: strawberry.Info = strawberry.UNSET) -> Response:
        try:
            SessionHandler(
                StrawberryHelper.extract_request(info).session
            ).clear_session()
        except Exception as e:
            return Response(**State.failure(str(e)).asdict)
        return Response(**State.ok().asdict)
