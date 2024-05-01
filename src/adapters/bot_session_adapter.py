from src.adapters.user_adapter import UserAdapter
from src.adapters.base_adapter import BaseAdapter
from src.finders.user_finder import UserFinder
from src.models.bot.bot_session import BotSession
from src.api.types.bot_session import BotSession as BotSessionType
from src.types.exception_types import ExceptionTypes


class BotSessionAdapter(BaseAdapter):
    @staticmethod
    def plug(model: BotSession) -> BotSessionType:
        user = UserFinder.by_id(model.user_id)
        if not user:
            raise Exception(ExceptionTypes.NO_SUCH_OBJECT_EXISTS)
        data = {
            "id": model.pk,
            "user": UserAdapter.plug(user),
            "data": model.data,
        }
        return BotSessionType(**data)
