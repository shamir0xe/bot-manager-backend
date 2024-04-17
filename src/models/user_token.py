from datetime import datetime
from redis_om import Field, HashModel


class UserToken(HashModel):
    user_id: str = Field(index=True, primary_key=True)
    token: str = Field(index=True)
    expiration_date: datetime = Field(index=True)
