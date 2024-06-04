from typing import List, Optional

from sqlalchemy.orm import Session
from adapters.local_repository.alch_user_token_adapter import AlchUserTokenAdapter
from models.local_repository.user.alch_user_token import AlchUserToken
from src.decorators.local_repository.db_session import db_session
from src.models.user.user_token import UserToken
from src.repositories.interfaces.base_user_token_repository import (
    BaseUserTokenRepository,
)
from src.types.exception_types import ExceptionTypes


class UserTokenLocalRepository(BaseUserTokenRepository):
    @db_session
    def read(self, session: Optional[Session] = None) -> List[UserToken]:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        alch_user_tokens = session.query(AlchUserToken).all()
        return [
            AlchUserTokenAdapter.plug(alch_user_token)
            for alch_user_token in alch_user_tokens
        ]

    @db_session
    def read_by_id(self, id: str, session: Optional[Session] = None) -> UserToken:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        alch_user_token = (
            session.query(AlchUserToken)
            .filter(AlchUserToken.user_id == id)
            .one_or_none()
        )
        if not alch_user_token:
            raise Exception(ExceptionTypes.USER_TOKEN_INVALID)
        return AlchUserTokenAdapter.plug(alch_user_token)

    @db_session
    def read_by_token(self, token: str, session: Optional[Session] = None) -> UserToken:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)

        return super().read_by_token(token)

    @db_session
    def create(self, entity: UserToken, session: Optional[Session] = None) -> UserToken:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)

        return super().create(entity)

    @db_session
    def update(self, entity: UserToken, session: Optional[Session] = None) -> UserToken:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)

        return super().update(entity)

    @db_session
    def delete(self, entity: UserToken, session: Optional[Session] = None) -> UserToken:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)

        return super().delete(entity)
