from typing import List
from src.database.factories.user_factory import UserFactory
from src.database.factories.base_factory import BaseFactory
from src.adapters.user_adapter import UserAdapter
from src.api.types.user import User as UserType


class UserTypeFactory(BaseFactory):
    def generate(self) -> List[UserType]:
        return [UserAdapter.plug(user) for user in UserFactory().generate()]
