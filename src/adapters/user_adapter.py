from src.adapters.base_adapter import BaseAdapter
from src.models.user import User as UserModel
from src.api.types.user import User as UserType


class UserAdapter(BaseAdapter):
    @staticmethod
    def plug(model: UserModel) -> UserType:
        if not model.pk:
            raise ValueError("No valid ID is provided")

        data = {
            "id": model.pk,
            "telegram_id": model.telegram_id,
            "name": model.name,
            "server_ids": model.server_ids or [],
        }

        return UserType(**data)
