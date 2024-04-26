from typing import List
from pydantic import BaseModel

from .button import Button


class Keyboard(BaseModel):
    buttons: List[List[Button]]
