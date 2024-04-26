from dataclasses import dataclass
from typing import List
from faker.providers import internet
from .base_factory import BaseFactory
from src.models.server.server import Server


@dataclass
class ServerFactory(BaseFactory):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.faker.add_provider(internet)

    def generate(self, chain: bool = True) -> List[Server]:
        servers = []
        for _ in range(self.count):
            servers += [
                Server(
                    address=self.faker.uri(),
                    owner_id=self.faker.uuid4(),
                    port=self.faker.port_number(),
                    server_ids=[
                        server.pk
                        for server in ServerFactory(self.count >> 1).generate(False)
                    ]
                    if chain
                    else [],
                )
            ]

        return servers
