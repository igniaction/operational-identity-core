"""
Identity operational context.
"""

from dataclasses import dataclass

from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.domain.entities.permission import (
    Permission,
)


@dataclass
class IdentityContext:
    """
    Aggregated operational identity context.
    """

    user: User

    roles: list[Role]

    permissions: list[Permission]
