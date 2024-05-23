import strawberry
from actions.user.login_user import LoginUser
from api.types.user import User
from resolvers.base_resolver import BaseResolver


class OtpResolver(BaseResolver):
    desc = "Login the user using otp"

    @staticmethod
    def fn(code: str = strawberry.UNSET, info: strawberry.Info = strawberry.UNSET) -> User:
        ClearSession(info=info)
        telegram_id = RetrieveUserFromOtpCode.retrieve(code=code)
        user_model = LoginUser.with_telegram_id(telegra_id=telegram_id)
        return UserAdapter.plug(user_model)



