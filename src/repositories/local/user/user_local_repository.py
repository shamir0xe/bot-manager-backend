from typing import List
from src.models.user.user import User
from src.repositories.repository import Repository


class UserLocalRepository(Repository):
    def read(self) -> List[User]:
        return super().read()
    
    def read_by_id(self, id: str) -> User:
        return super().read_by_id(id)
    
    def create(self, entity: User) -> User:
        return super().create(entity)

    def update(self, entity: User) -> User:
        return super().create(entity)

    def delete(self, entity: User) -> User:
        return super().delete(entity)
