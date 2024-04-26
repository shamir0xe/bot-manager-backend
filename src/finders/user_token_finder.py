from redis_om import Migrator
from src.models.user.user_token import UserToken


class UserTokenFinder:
    @staticmethod
    def with_user_id(user_id: str) -> UserToken:
        print(f"searching for {user_id}")
        # Migrator().run()
        user_token = UserToken.find(UserToken.user_id == user_id).first()
        print(user_token)
        if not isinstance(user_token, UserToken):
            raise Exception("No such user_token pair found with the provided user_id")
        return user_token

    @staticmethod
    def with_token(token: str) -> UserToken:
        user_token = UserToken.find(UserToken.token == token).first()
        if not isinstance(user_token, UserToken):
            raise Exception("No such user_token pair found with the provided token")
        return user_token
