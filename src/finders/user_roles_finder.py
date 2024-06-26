from src.models.user.user_roles import UserRoles


class UserRolesFinder:
    @staticmethod
    def with_user_id(user_id: str) -> UserRoles:
        user_roles = UserRoles.find(UserRoles.user_id == user_id).first()
        if not isinstance(user_roles, UserRoles):
            raise Exception("No such user_roles found")
        return user_roles
