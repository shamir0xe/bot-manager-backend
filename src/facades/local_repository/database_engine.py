from sqlalchemy import Engine
from src.helpers.decorators.singleton import singleton
from src.actions.database.create_engine_and_tables import CreateEngineAndTables


@singleton
class DatabaseEngine:
    engine: Engine

    def __init__(self) -> None:
        self.engine = CreateEngineAndTables.create()
