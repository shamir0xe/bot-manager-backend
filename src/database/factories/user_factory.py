from dataclasses import dataclass
from typing import List
from faker.providers import internet
from src.database.factories.server_factory import ServerFactory
from src.models.user.user import User
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
                    telegram_id=self.faker.ascii_email(),
                    name=self.faker.user_name(),
                    server_ids=[
                        server.pk
                        for server in ServerFactory(
                            count=max(self.count >> 1, 1)
                        ).generate()
                    ],
                )
            ]
        return users
