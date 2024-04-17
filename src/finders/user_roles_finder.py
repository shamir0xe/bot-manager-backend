from typing import List

from redis_om import Migrator

from src.models.user_roles import UserRoles


class UserRolesFinder:
    @staticmethod
    def with_user_id(user_id: str) -> UserRoles:
        # TODO: move Migrator to the seeders section
        Migrator().run()
        user_roles = UserRoles.find(UserRoles.user_id == user_id).first()
        if not isinstance(user_roles, UserRoles):
            raise Exception("No such user_roles found")
        return user_roles
