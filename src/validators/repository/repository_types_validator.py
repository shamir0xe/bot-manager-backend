from types.exception_types import ExceptionTypes
from types.repository_types import RepositoryTypes


class RepositoryTypesValidator:
    @staticmethod
    def validate(obj: str) -> RepositoryTypes:
        if obj.lower() == "local":
            return RepositoryTypes.LOCAL
        if obj.lower() == "api":
            return RepositoryTypes.API
        raise Exception(ExceptionTypes.REPOSITORY_NOT_SUPPORTED)
