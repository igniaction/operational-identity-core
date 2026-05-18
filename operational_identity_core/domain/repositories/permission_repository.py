"""
Permission repository contract.
"""

from abc import ABC
from abc import abstractmethod

from operational_identity_core.domain.entities.permission import (
    Permission,
)


class PermissionRepository(ABC):
    """
    Permission repository contract.
    """

    @abstractmethod
    def find_by_name(
        self,
        name: str,
    ) -> Permission | None:
        """
        Find permission by name.
        """
