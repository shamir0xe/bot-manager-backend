import uuid
from typing import List
from src.database.factories.base_factory import BaseFactory
from src.models.user_token import UserToken


class UserTokenFactory(BaseFactory):
    def generate(self) -> List[UserToken]:
        tokens = []
        for _ in range(self.count):
            tokens += [
                UserToken(
                    user_id=self.faker.uuid4(),
                    token=uuid.uuid4().hex,
                    expiration_date=self.faker.date_time(),
                )
            ]
        return tokens
