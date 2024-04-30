from src.helpers.config.config import Config
from src.helpers.decorators.singleton import singleton
from src.models.utility.env_data import EnvData


@singleton
class Env:
    env: EnvData

    def __init__(self) -> None:
        self.env = EnvData(**Config.read("env"))

    @property
    def project_name(self):
        return self.env.project_name

    @property
    def debug(self):
        return self.env.debug

    @property
    def session_key(self):
        return self.env.session.secret_key

    @property
    def db(self):
        return self.env.db
