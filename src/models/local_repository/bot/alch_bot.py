from typing import TYPE_CHECKING, Annotated, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.actions.database.generate_id import GenerateId
from src.models.local_repository.alch_base import AlchBase

if TYPE_CHECKING:
    from src.models.local_repository.user.alch_user import AlchUser

AAU = Annotated["AlchUser", AlchUser]


class AlchBot(AlchBase):
    __tablename__ = "bots"

    id: Mapped[str] = mapped_column(primary_key=True, default=GenerateId.generate)
    name: Mapped[str]
    token: Mapped[str]
    host: Mapped[str]
    port: Mapped[int]
    pages: Mapped[str]
    user: Mapped[AAU] = relationship(back_populates="bots")

    def __repr__(self) -> str:
        return f"""alch-bot{self.created_at}-{self.updated_at}-
        {self.id}-{self.name}{self.token}"""
