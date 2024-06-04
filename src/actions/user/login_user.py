from typing import Optional
from src.actions.user.create_user import CreateUser
from src.finders.user_finder import UserFinder
from src.models.user.user import User
from src.helpers.state_manager import State
from src.mediators.token_mediator import TokenMediator


class LoginUser:
    @staticmethod
    def login_or_register(telegram_id: str, name: Optional[str] = None) -> User:
        user_model = UserFinder.by_telegram_id(telegram_id)
        if not user_model:
            user_model = CreateUser.with_telegram_id(telegram_id=telegram_id, name=name)
        user_model = LoginUser.login(telegram_id=telegram_id)
        return user_model

    @staticmethod
    def login(telegram_id: str) -> User:
        """We are assure that user with telegram_id exists, now log them in"""
        mediator = TokenMediator.with_user_id(telegram_id).check_expiration()
        if not mediator.state.is_ok:
            ## either:
            # 1) token is not set, or
            # 2) got expired
            mediator.state = State.ok()
            mediator.revoke_token().save()
        return mediator.retrieve_user()
