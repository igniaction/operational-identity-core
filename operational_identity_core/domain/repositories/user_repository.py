"""
User repository contract.
"""

from abc import ABC
from abc import abstractmethod

from operational_identity_core.domain.entities.user import (
    User,
)


class UserRepository(ABC):
    """
    User repository contract.
    """

    @abstractmethod
    def save(
        self,
        user: User,
    ) -> None:
        """
        Persist user.
        """

    @abstractmethod
    def find_by_username(
        self,
        username: str,
    ) -> User | None:
        """
        Find user by username.
        """
