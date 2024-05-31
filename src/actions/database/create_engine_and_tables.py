from sqlalchemy import Engine, create_engine
from src.facades.env import Env
from src.helpers.config.config import Config
from src.models.local_repository.alch_base import AlchBase


class CreateEngineAndTables:
    @staticmethod
    def create() -> Engine:
        engine = create_engine(
            url=f"sqlite+pysqlite:///{Config.read('main.sql.path')}", echo=Env().debug
        )
        AlchBase.metadata.create_all(engine)
        return engine
