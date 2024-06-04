from typing import TYPE_CHECKING, Annotated, List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.local_repository.alch_base import AlchBase

if TYPE_CHECKING:
    from src.models.local_repository.bot.alch_bot import AlchBot

AAB = Annotated["AlchBot", AlchBot]


class AlchUser(AlchBase):
    __tablename__ = "users"

    telegram_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    bots: Mapped[List[AAB]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"""alch-user{self.created_at}-{self.updated_at}-
        {self.telegram_id}-{self.name}"""
