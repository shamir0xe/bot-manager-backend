from src.adapters.base_adapter import BaseAdapter
from src.models.local_repository.user.alch_user_token import AlchUserToken
from src.models.user.user_token import UserToken


class AlchUserTokenAdapter(BaseAdapter):
    @staticmethod
    def plug(model: AlchUserToken) -> UserToken:
        return UserToken(
            user_id=model.user_id,
            token=model.token,
            expiration_date=model.expiration_date,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
