"""
Assemble identity context use case.
"""

from operational_identity_core.application.dto.identity_context_dto import (
    IdentityContextDTO,
)

from operational_identity_core.domain.repositories.role_repository import (
    RoleRepository,
)

from operational_identity_core.domain.repositories.user_repository import (
    UserRepository,
)

from operational_identity_core.domain.services.permission_resolution_service import (
    PermissionResolutionService,
)


class AssembleIdentityContextUseCase:
    """
    Assemble operational identity context.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        role_repository: RoleRepository,
    ) -> None:

        self.user_repository = (
            user_repository
        )

        self.role_repository = (
            role_repository
        )

        self.permission_service = (
            PermissionResolutionService()
        )

    def execute(
        self,
        username: str,
    ) -> IdentityContextDTO:
        """
        Assemble operational context.
        """

        user = (
            self.user_repository.find_by_username(
                username,
            )
        )

        if user is None:
            raise ValueError(
                "User not found.",
            )

        roles = (
            self.role_repository.find_roles_by_user(
                str(user.id),
            )
        )

        permissions = (
            self.permission_service.resolve(
                roles,
            )
        )

        return IdentityContextDTO(
            user_id=str(user.id),
            username=user.username.value,
            permissions=[
                permission.name
                for permission in permissions
            ],
        )
