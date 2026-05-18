"""
Permission mapper.
"""

from uuid import UUID

from operational_identity_core.domain.entities.permission import (
    Permission,
)

from operational_identity_core.infrastructure.persistence.permission_model import (
    PermissionModel,
)


class PermissionMapper:
    """
    Translate Permission ORM <-> Domain.
    """

    @staticmethod
    def to_domain(
        model: PermissionModel,
    ) -> Permission:

        return Permission(
            id=UUID(model.id),
            name=model.name,
        )

    @staticmethod
    def to_model(
        entity: Permission,
    ) -> PermissionModel:

        return PermissionModel(
            id=str(entity.id),
            name=entity.name,
        )
