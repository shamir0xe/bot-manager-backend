import strawberry

from src.authorizations.handlers.session_handler import SessionHandler
from src.helpers.strawberry.strawberry_helper import StrawberryHelper


class ClearSession:
    @staticmethod
    def clear(info: strawberry.Info) -> None:
        SessionHandler(StrawberryHelper.extract_request(info).session).clear_session()
