from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Dict, Optional
from src.helpers.types.status_types import StatusType


@dataclass
class State:
    status: StatusType
    message: Optional[str] = ""

    @classmethod
    def ok(cls, message: str="") -> State:
        return State(StatusType.OK, message)

    @classmethod
    def failure(cls, message: str = "") -> State:
        return State(StatusType.FAILED, message)

    @property
    def is_ok(self) -> bool:
        return self.status == StatusType.OK

    @property
    def asdict(self) -> Dict:
        return asdict(self)
