from pydantic import BaseModel


class DataBase(BaseModel):
    host: str
    port: int
