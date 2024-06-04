from typing import Annotated
from pydantic import BaseModel, BeforeValidator

from src.models.utility.data_base import DataBase
from src.models.utility.session_data import SessionData
from src.types.repository_types import RepositoryTypes
from src.validators.repository.repository_types_validator import (
    RepositoryTypesValidator,
)

RT = Annotated[RepositoryTypes, BeforeValidator(RepositoryTypesValidator.validate)]


class EnvData(BaseModel):
    project_name: str
    debug: bool
    session: SessionData
    db: DataBase
    repository: RT
