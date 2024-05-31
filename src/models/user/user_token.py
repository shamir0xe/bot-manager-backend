from datetime import datetime
from src.models.utility.decorated_base_model import DecoratedBaseModel


class UserToken(DecoratedBaseModel):
    user_id: str # pk
    token: str
    expiration_date: datetime

    # class Meta:  # type: ignore
    #     model_key_prefix = "user_tokens"
