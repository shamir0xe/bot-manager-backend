from src.api.types.response import Response
from src.mediators.seeder_mediator import SeederMediator
from src.resolvers.base_resolver import BaseResolver


class RunSeedersResolver(BaseResolver):
    desc = "Running seeders, [dev] scope"

    @staticmethod
    def fn() -> Response:
        return Response(**SeederMediator().seed_super_admins().get_state().asdict)
