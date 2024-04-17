from src.finders.user_roles_finder import UserRolesFinder
from src.helpers.state_manager import State
from src.helpers.types.user_roles import UserRoles
from src.policies.base_policy import BasePolicy


class AdminPolicy(BasePolicy):
    role = UserRoles.ADMIN.name.lower()

    @staticmethod
    def check(user_id: str = "") -> State:
        try:
            roles = UserRolesFinder.with_user_id(user_id).roles
        except Exception:
            return State.failure("Not permitted")
        return (
            State.ok() if AdminPolicy.role in roles else State.failure("Not an admin")
        )
