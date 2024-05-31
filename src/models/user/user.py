from typing import Optional

from pydantic import Field
from src.models.utility.decorated_base_model import DecoratedBaseModel


class User(DecoratedBaseModel):
    telegram_id: str # pk
    name: Optional[str] = Field(default="")

    # class Meta:  # type: ignore
    #     model_key_prefix = "users"
