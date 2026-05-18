"""
Resolve permissions use case.
"""

from operational_identity_core.domain.repositories.role_repository import (
    RoleRepository,
)

from operational_identity_core.domain.services.permission_resolution_service import (
    PermissionResolutionService,
)


class ResolvePermissionsUseCase:
    """
    Resolve operational permissions.
    """

    def __init__(
        self,
        role_repository: RoleRepository,
    ) -> None:

        self.role_repository = role_repository

        self.permission_service = (
            PermissionResolutionService()
        )

    def execute(
        self,
        user_id: str,
    ) -> list[str]:
        """
        Resolve permissions from roles.
        """

        roles = (
            self.role_repository.find_roles_by_user(
                user_id,
            )
        )

        permissions = (
            self.permission_service.resolve(
                roles,
            )
        )

        return [
            permission.name
            for permission in permissions
        ]
