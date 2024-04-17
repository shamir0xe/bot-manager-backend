from src.helpers.types.authentication_types import AuthenticationTypes


class AuthenticationMapper:
    @staticmethod
    def map(auth_type: AuthenticationTypes):
        return auth_type.name
