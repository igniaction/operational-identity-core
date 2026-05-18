"""
Permission resolution service.
"""

from operational_identity_core.domain.entities.permission import (
    Permission,
)

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.infrastructure.logging.runtime_logger import (
    logger,
)


class PermissionResolutionService:
    """
    Resolve aggregated permissions from roles.
    """

    def resolve(
        self,
        roles: list[Role],
    ) -> list[Permission]:
        """
        Aggregate permissions from all roles.
        """

        logger.info(
            "PERMISSION_AGGREGATION started",
        )

        permissions_map: dict[str, Permission] = {}

        for role in roles:

            logger.info(
                "ROLE_RESOLUTION role=%s",
                role.name,
            )

            for permission in role.permissions:

                logger.info(
                    "PERMISSION_FOUND permission=%s",
                    permission.name,
                )

                permissions_map[
                    permission.name
                ] = permission

        logger.info(
            "PERMISSION_AGGREGATION completed total=%s",
            len(permissions_map),
        )

        return list(
            permissions_map.values(),
        )
