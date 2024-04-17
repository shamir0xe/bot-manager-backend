from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class SessionHandler:
    session: Dict[str, Any]

    def is_authorized(self, token: str) -> bool:
        if "is_auth" not in self.session or "user_id" not in self.session:
            return False
        return self.session.get("user_id") == token

    def inject_dict(self, data: Dict[str, Any]) -> None:
        self.session.update(data)

    @property
    def user_id(self) -> str:
        return self.session.get("user_id", "")

    def clear_session(self) -> None:
        for key in self.session.keys():
            self.session[f"{key}"] = ""
