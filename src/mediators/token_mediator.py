from __future__ import annotations
from dataclasses import dataclass, field

from src.helpers.types.status_types import StatusType
from src.delegators.datetime_delegator import DatetimeDelegator
from src.finders.user_token_finder import UserTokenFinder
from src.database.factories.user_token_factory import UserTokenFactory
from src.models.user.user_token import UserToken
from src.helpers.state_manager import State


@dataclass
class TokenMediator:
    user_id: str = field(default="")
    token: str = field(default="")
    user_token: UserToken = field(default_factory=UserTokenFactory().get_one)
    state: State = field(default_factory=State.ok)

    @classmethod
    def with_user_id(cls, user_id: str) -> TokenMediator:
        print(f"token_mediator with_user_id {user_id}")
        mediator = TokenMediator(user_id=user_id)
        mediator = mediator.retrieve_token()
        return mediator

    @classmethod
    def with_token(cls, token: str) -> TokenMediator:
        mediator = TokenMediator(token=token)
        mediator = mediator.retrieve_user_id()
        return mediator

    def retrieve_token(self) -> TokenMediator:
        if not self.state.is_ok:
            return self
        try:
            print(f"finding token for this user: {self.user_id}")
            self.user_token = UserTokenFinder.with_user_id(self.user_id)
            print(f"retrieved user_token, with token: {self.user_token.token}")
            if not self.user_token:
                raise Exception("user_token pair does'nt exist")
            self.token = self.user_token.token
        except Exception as e:
            print(e)
            self.state = State.failure(str(e))
        return self

    def retrieve_user_id(self) -> TokenMediator:
        if not self.state.is_ok:
            return self
        try:
            print(f"going to retrieve the user with this token: {self.token}")
            self.user_token = UserTokenFinder.with_token(self.token)
            print(self.user_token)
            if not self.user_token:
                raise Exception("user_token pair does'nt exist")
            self.user_id = self.user_token.user_id
        except Exception as e:
            self.state = State.failure(str(e))
        return self

    def check_expiration(self) -> TokenMediator:
        if not self.state.is_ok:
            return self
        if not DatetimeDelegator.valid_due_date(self.user_token.expiration_date):
            self.state = State(StatusType.FAILED, "Expired token")
        return self

    def revoke_token(self) -> TokenMediator:
        if not self.state.is_ok:
            return self
        self.user_token = UserTokenFactory().get_one()
        self.user_token.user_id = self.user_id
        self.user_token.expiration_date = DatetimeDelegator.expiration_from_now()
        print("here")
        return self

    def save(self) -> TokenMediator:
        if not self.state.is_ok:
            return self
        self.user_token.save()
        print("after save")
        print(self.user_token.Meta.index_name)
        return self

    def get_token(self) -> str:
        if not self.state.is_ok:
            return ""
        return self.user_token.token
