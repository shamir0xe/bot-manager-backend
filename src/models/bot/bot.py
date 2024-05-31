from typing import Optional

from pydantic import Field
from src.models.utility.decorated_base_model import DecoratedBaseModel


class Bot(DecoratedBaseModel):
    id: str # pk
    name: str
    token: str
    host: Optional[str] = Field(default="")
    port: Optional[int] = Field(default=0)
    pages: Optional[str] = Field(default="")

    # class Meta:  # type: ignore
    #     model_key_prefix = "bots"
