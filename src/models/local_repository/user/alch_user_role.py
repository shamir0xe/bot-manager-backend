from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from actions.database.generate_id import GenerateId
from src.models.local_repository.alch_base import AlchBase


class AlchUserRole(AlchBase):
    __tablename__ = "user_roles"

    id: Mapped[str] = mapped_column(primary_key=True, default=GenerateId.generate)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.telegram_id"))
    role: Mapped[str]

    def __repr__(self) -> str:
        return f"{self.created_at}|{self.updated_at}|{self.user_id}|{self.role}"
