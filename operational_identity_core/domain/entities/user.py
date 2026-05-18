"""
User entity.
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from operational_identity_core.domain.value_objects.email import (
    Email,
)

from operational_identity_core.domain.value_objects.username import (
    Username,
)

from operational_identity_core.domain.value_objects.identity_status import (
    IdentityStatus,
)


@dataclass
class User:
    """
    Operational identity entity.
    """

    email: Email
    username: Username

    id: UUID = field(default_factory=uuid4)

    status: IdentityStatus = IdentityStatus.PENDING

    def activate(self) -> None:
        """
        Activate identity.
        """

        self.status = IdentityStatus.ACTIVE

    def disable(self) -> None:
        """
        Disable identity.
        """

        self.status = IdentityStatus.DISABLED

    @property
    def is_active(self) -> bool:
        """
        Check active state.
        """

        return self.status == IdentityStatus.ACTIVE
