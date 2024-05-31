from typing import List

from pydantic import Field
from src.models.utility.decorated_base_model import DecoratedBaseModel


class UserRoles(DecoratedBaseModel):
    user_id: str # pk
    roles: List[str] = Field(default=[])

    # class Meta:  # type: ignore
    #     model_key_prefix = "user_roles"
