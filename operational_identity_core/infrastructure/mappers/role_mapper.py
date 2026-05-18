"""
Role mapper.
"""

from uuid import UUID

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.infrastructure.mappers.permission_mapper import (
    PermissionMapper,
)

from operational_identity_core.infrastructure.persistence.role_model import (
    RoleModel,
)


class RoleMapper:
    """
    Translate Role ORM <-> Domain.
    """

    @staticmethod
    def to_domain(
        model: RoleModel,
    ) -> Role:

        permissions = [
            PermissionMapper.to_domain(
                permission,
            )
            for permission in model.permissions
        ]

        return Role(
            id=UUID(model.id),
            name=model.name,
            permissions=permissions,
        )

    @staticmethod
    def to_model(
        entity: Role,
    ) -> RoleModel:

        return RoleModel(
            id=str(entity.id),
            name=entity.name,
        )
