"""
Role repository contract.
"""

from abc import ABC
from abc import abstractmethod

from operational_identity_core.domain.entities.role import (
    Role,
)


class RoleRepository(ABC):
    """
    Role repository contract.
    """

    @abstractmethod
    def find_roles_by_user(
        self,
        user_id: str,
    ) -> list[Role]:
        """
        Resolve roles from user.
        """

    @abstractmethod
    def save(
        self,
        role: Role,
    ) -> None:
        """
        Persist role.
        """
