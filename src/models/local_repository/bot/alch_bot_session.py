from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.actions.database.generate_id import GenerateId
from src.models.local_repository.alch_base import AlchBase


class AlchBotSession(AlchBase):
    __tablename__ = "bot_sessions"

    id: Mapped[str] = mapped_column(primary_key=True, default=GenerateId.generate)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.telegram_id"))
    bot_id: Mapped[str] = mapped_column(ForeignKey("bots.id"))
    data: Mapped[str]

    def __repr__(self) -> str:
        return f"""alch-bot{self.created_at}-{self.updated_at}-
        {self.id}-{self.user_id}{self.bot_id}-{self.data}"""
