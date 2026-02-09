from abc import ABC, abstractmethod

from src.domain.user.user import User


class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> User: ...

    @abstractmethod
    def get_by_username(self, username: str) -> User | None: ...

    @abstractmethod
    def get_by_email(self, email: str) -> User | None: ...
