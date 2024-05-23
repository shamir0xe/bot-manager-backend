from typing import Optional
from src.actions.user.create_user import CreateUser
from src.finders.user_finder import UserFinder
from src.models.user.user import User
from src.helpers.state_manager import State
from src.mediators.token_mediator import TokenMediator
from src.types.exception_types import ExceptionTypes


class LoginUser:
    @staticmethod
    def with_user_id(user_id: str) -> State:
        mediator = TokenMediator.with_user_id(user_id).check_expiration()
        if not mediator.state.is_ok:
            ## either:
            # 1) token is not set, or
            # 2) got expired
            mediator.state = State.ok()
            mediator.revoke_token().save()
        return mediator.state

    @staticmethod
    def with_telegram_id(telegram_id: str, name: Optional[str] = None) -> User:
        user_model = UserFinder.by_telegram_id(telegram_id)
        if not user_model:
            user_model = CreateUser.with_telegram_id(telegram_id=telegram_id, name=name)
        if not user_model.id:
            raise Exception(ExceptionTypes.INTERNAL_ERROR)
        state = LoginUser.with_user_id(user_model.id)
        if not state.is_ok:
            raise Exception(ExceptionTypes.LOGIN_ERROR)
        return user_model
