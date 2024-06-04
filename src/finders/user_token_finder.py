from src.models.user.user_token import UserToken


class UserTokenFinder:
    @staticmethod
    def with_user_id(user_id: str) -> UserToken:
        user_token = UserTokenRepository().read_by_id(user_id)
        if not isinstance(user_token, UserToken):
            raise Exception("No such user_token pair found with the provided user_id")
        return user_token

    @staticmethod
    def with_token(token: str) -> UserToken:
        user_token = UserTokenRepository().read_by_token(token)
        if not isinstance(user_token, UserToken):
            raise Exception("No such user_token pair found with the provided token")
        return user_token
