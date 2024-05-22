from src.api.types.response import Response
from src.mediators.seeder_mediator import SeederMediator


class RunSeeders:
    """Run Database Seeders"""

    @staticmethod
    def run() -> Response:
        resopnse = SeederMediator().seed_super_admins().get_state().asdict
        return Response(**resopnse)
