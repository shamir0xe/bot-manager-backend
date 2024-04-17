from __future__ import annotations
from dataclasses import dataclass, field

from src.database.seeders.super_admin_seeder import SuperAdminSeeder
from src.helpers.state_manager import State


@dataclass
class SeederMediator:
    state: State = field(default_factory=State.ok)

    def seed_super_admins(self) -> SeederMediator:
        if not self.state.is_ok:
            return self
        try:
            result = SuperAdminSeeder.seed()
            self.state = result
        except Exception as e:
            self.state = State.failure(str(e))
        return self

    def get_state(self) -> State:
        return self.state
