from typing import List, Optional
from sqlalchemy import delete, update
from sqlalchemy.orm import Session
from src.facades.repository.user.user_repository import UserRepository
from src.models.local_repository.bot.alch_bot import AlchBot
from src.adapters.local_repository.alch_user_adapter import AlchUserAdapter
from src.models.local_repository.user.alch_user import AlchUser
from src.decorators.local_repository.db_session import db_session
from src.models.user.user import User
from src.types.exception_types import ExceptionTypes


class UserLocalRepository(UserRepository):
    @db_session
    def read(self, session: Optional[Session] = None) -> List[User]:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        alch_users = session.query(AlchUser).all()
        return [AlchUserAdapter.plug(alch_user) for alch_user in alch_users]

    @db_session
    def read_by_matched_bot(
        self, bot_id: str, session: Optional[Session] = None
    ) -> User:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        alch_bot = session.query(AlchBot).filter(AlchBot.id == bot_id).one_or_none()
        if not alch_bot:
            raise Exception(ExceptionTypes.NO_BOT_AVAILABLE)
        return AlchUserAdapter.plug(alch_bot.user)

    @db_session
    def read_by_id(self, id: str, session: Optional[Session] = None) -> User:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        alch_user = (
            session.query(AlchUser).filter(AlchUser.telegram_id == id).one_or_none()
        )
        if not alch_user:
            raise Exception(ExceptionTypes.USER_INVALID)
        return AlchUserAdapter.plug(alch_user)

    @db_session
    def create(self, entity: User, session: Optional[Session] = None) -> User:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        alch_user = AlchUser(**entity.model_dump())
        session.add(alch_user)
        session.flush()
        return AlchUserAdapter.plug(alch_user)

    @db_session
    def update(self, entity: User, session: Optional[Session] = None) -> User:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        stmt = (
            update(AlchUser)
            .where(AlchUser.telegram_id == entity.telegram_id)
            .values(**entity.model_dump())
            .returning(AlchUser)
        )
        alch_user = session.scalar(stmt)
        if not alch_user:
            raise Exception(ExceptionTypes.USER_UPDATE_ERROR)
        return AlchUserAdapter.plug(alch_user)

    @db_session
    def delete(self, entity: User, session: Optional[Session] = None) -> User:
        if not session:
            raise Exception(ExceptionTypes.DB_LOST_CONNECTION)
        stmt = (
            delete(AlchUser)
            .where(AlchUser.telegram_id == entity.telegram_id)
            .returning(AlchUser)
        )
        alch_user = session.scalar(stmt)
        if not alch_user:
            raise Exception(ExceptionTypes.USER_DELETE_ERROR)
        return AlchUserAdapter.plug(alch_user)
