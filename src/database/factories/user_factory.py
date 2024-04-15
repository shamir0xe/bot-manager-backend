import uuid
from dataclasses import dataclass
from typing import List
from faker.providers import internet
import strawberry
from src.api.types.user import User
from .base_factory import BaseFactory


@dataclass
class UserFactory(BaseFactory):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.faker.add_provider(internet)

    def generate(self) -> List[User]:
        users = []
        for _ in range(self.count):
            users += [
                User(
                    id=strawberry.ID(uuid.uuid4().__str__()),
                    telegram_id=self.faker.ascii_email(),
                    name=self.faker.user_name(),
                    server_ids=[],
                )
            ]
        return users
