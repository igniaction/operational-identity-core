"""
Role entity.
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from operational_identity_core.domain.entities.permission import (
    Permission,
)


@dataclass
class Role:
    """
    Organizational role entity.
    """

    name: str

    permissions: list[Permission] = field(default_factory=list)

    id: UUID = field(default_factory=uuid4)

    def add_permission(
        self,
        permission: Permission,
    ) -> None:
        """
        Attach permission to role.
        """

        self.permissions.append(permission)
