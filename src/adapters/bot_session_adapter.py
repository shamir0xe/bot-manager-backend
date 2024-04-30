from src.adapters.bot_adapter import BotAdapter
from src.adapters.user_adapter import UserAdapter
from src.models.bot.bot import Bot
from src.models.user.user import User
from src.adapters.base_adapter import BaseAdapter
from src.finders.bot_finder import BotFinder
from src.finders.user_finder import UserFinder
from src.models.bot.bot_session import BotSession
from src.api.types.bot_session import BotSession as BotSessionType
from src.types.exception_types import ExceptionTypes


class BotSessionAdapter(BaseAdapter):
    @staticmethod
    def plug(model: BotSession) -> BotSessionType:
        user = UserFinder.by_id(model.user_id)
        bot = BotFinder.by_id(model.bot_id)
        if not user or not bot:
            raise Exception(ExceptionTypes.NO_SUCH_PAIR_FOUND)
        data = {
            "id": model.pk,
            "user": UserAdapter.plug(user),
            "bot": BotAdapter.plug(bot),
            "data": model.data,
        }
        return BotSessionType(**data)

    @staticmethod
    def plug_with_objects(model: BotSession, user: User, bot: Bot) -> BotSessionType:
        return BotSessionType(
            **{
                "id": model.pk,
                "user": UserAdapter.plug(user),
                "bot": BotAdapter.plug(bot),
                "data": model.data,
            }
        )
