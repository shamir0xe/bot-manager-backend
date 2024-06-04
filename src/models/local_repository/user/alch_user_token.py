from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.models.local_repository.alch_base import AlchBase


class AlchUserToken(AlchBase):
    __tablename__ = "user_tokens"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.telegram_id"), primary_key=True
    )
    token: Mapped[str]
    expiration_date: Mapped[datetime]

    def __repr__(self) -> str:
        return f"""{self.token}|{self.user_id}|{self.expiration_date}|
        {self.updated_at}|{self.created_at}"""
