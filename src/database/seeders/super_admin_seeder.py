from src.finders.user_roles_finder import UserRolesFinder
from src.models.user.user_roles import UserRoles
from src.database.factories.user_factory import UserFactory
from src.finders.user_finder import UserFinder
from src.helpers.state_manager import State


class SuperAdminSeeder:
    super_admins = [
        {
            "telegram_id": "@shamir0xe",
            "name": "Amirhossein Shapoori",
        },
        {"telegram_id": "@mobinadrb", "name": "Mobina Darabi"},
        {"telegram_id": "@botfather", "name": "Bot father, from another mother"},
    ]

    @staticmethod
    def seed() -> State:
        for user_data in SuperAdminSeeder.super_admins:
            # updating/creating user info
            user = UserFinder.by_telegram_id(user_data["telegram_id"])
            if not user:
                user = UserFactory().get_one()
                user.server_ids = []
            user.telegram_id = user_data["telegram_id"]
            user.name = user_data["name"]
            user.save()
            if not isinstance(user.pk, str):
                return State.failure("Can't assign pk to the user")

            # updating/creating super_admins roles
            try:
                user_roles = UserRolesFinder.with_user_id(user.pk)
                if "admin" not in user_roles.roles:
                    user_roles.roles += ["admin"]
            except Exception:
                user_roles = UserRoles(user_id=user.pk, roles=["admin"])
            user_roles.save()
        return State.ok()
