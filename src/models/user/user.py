from typing import TYPE_CHECKING, Annotated, List, Optional

from pydantic import Field
from src.models.utility.decorated_base_model import DecoratedBaseModel

if TYPE_CHECKING:
    from src.models.bot.bot import Bot

AB = Annotated["Bot", Bot]


class User(DecoratedBaseModel):
    telegram_id: str  # pk
    name: Optional[str] = Field(default="")
    # bots: List[AB]
