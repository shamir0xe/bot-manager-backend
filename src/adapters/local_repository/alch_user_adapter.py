from src.adapters.base_adapter import BaseAdapter
from src.models.local_repository.user.alch_user import AlchUser
from src.models.user.user import User


class AlchUserAdapter(BaseAdapter):
    @staticmethod
    def plug(model: AlchUser) -> User:
        return User(
            telegram_id=model.telegram_id,
            name=model.name,
            created_at=model.created_at,
            updated_at=model.updated_at,
            # bots=[AlchBotAdapter.plug(bot) for bot in model.bots]
        )
