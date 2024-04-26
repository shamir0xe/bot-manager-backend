from pydantic import BaseModel


class SessionData(BaseModel):
    secret_key: str
