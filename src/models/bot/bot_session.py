from src.models.utility.decorated_base_model import DecoratedBaseModel


class BotSession(DecoratedBaseModel):
    id: str # pk
    user_id: str
    bot_id: str
    data: str

    # class Meta:  # type: ignore
    #     model_key_prefix = "bot_sessions"
