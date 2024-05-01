import strawberry
from src.finders.bot_session_finder import BotSessionFinder
from src.adapters.bot_session_adapter import BotSessionAdapter
from src.actions.user.create_user import CreateUser
from src.finders.bot_finder import BotFinder
from src.finders.user_finder import UserFinder
from src.helpers.types.user_roles import UserRoles
from src.models.bot.bot_session import BotSession
from src.api.types.bot_session import BotSession as BotSessionType
from src.resolvers.base_resolver import BaseResolver
from src.authorizations.authorization import role
from src.types.exception_types import ExceptionTypes


class RequestBotSessionResolver(BaseResolver):
    desc = "Request new bot session"

    @role(UserRoles.ADMIN)
    @staticmethod
    def fn(
        bot_id: str = strawberry.UNSET,
        telegram_id: str = strawberry.UNSET,
        info: strawberry.Info = strawberry.UNSET,
    ) -> BotSessionType:
        bot = BotFinder.by_id(bot_id)
        if not bot:
            raise Exception(ExceptionTypes.NO_SUCH_OBJECT_EXISTS)
        user = UserFinder.by_telegram_id(telegram_id)
        if not user:
            user = CreateUser.with_telegram_id(telegram_id)
            if not user:
                raise Exception(ExceptionTypes.INTERNAL_ERROR)
        if not user.pk:
            raise Exception(ExceptionTypes.INTERNAL_ERROR)
        # check if the last user's session of this bot is empty
        bot_session = BotSessionFinder.last_user_session(bot_id=bot.id, user_id=user.pk)
        if bot_session and not bot_session.data:
            # if the conditions was true, return the last session
            return BotSessionAdapter.plug(bot_session)
        data = {"user_id": user.pk, "bot_id": bot.id, "data": ""}
        bot_session = BotSession(**data)
        bot_session.save()
        if not bot_session.pk:
            raise Exception(ExceptionTypes.INTERNAL_ERROR)
        return BotSessionAdapter.plug(bot_session)
