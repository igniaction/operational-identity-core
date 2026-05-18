"""
Identity resolution service.
"""

from operational_identity_core.domain.entities.identity_context import (
    IdentityContext,
)

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.services.permission_resolution_service import (
    PermissionResolutionService,
)

from operational_identity_core.infrastructure.logging.runtime_logger import (
    logger,
)


class IdentityResolutionService:
    """
    Resolve operational identity context.
    """

    def __init__(self) -> None:

        self.permission_service = (
            PermissionResolutionService()
        )

    def resolve(
        self,
        user: User,
        roles: list[Role],
    ) -> IdentityContext:
        """
        Resolve aggregated operational identity.
        """

        logger.info(
            "IDENTITY_RESOLUTION user=%s",
            user.username.value,
        )

        permissions = (
            self.permission_service.resolve(
                roles=roles,
            )
        )

        logger.info(
            "IDENTITY_CONTEXT_ASSEMBLED permissions=%s",
            len(permissions),
        )

        return IdentityContext(
            user=user,
            roles=roles,
            permissions=permissions,
        )
