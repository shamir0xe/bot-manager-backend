from pydantic import BaseModel

from src.models.utility.data_base import DataBase
from src.models.utility.session_data import SessionData


class EnvData(BaseModel):
    project_name: str
    debug: bool
    session: SessionData
    db: DataBase

