from operational_identity_core.domain.entities.permission import (
    Permission,
)

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.domain.services.permission_resolution_service import (
    PermissionResolutionService,
)


def test_should_aggregate_permissions() -> None:

    read_permission = Permission(
        name="READ_USERS",
    )

    write_permission = Permission(
        name="WRITE_USERS",
    )

    admin_role = Role(
        name="ADMIN",
    )

    admin_role.add_permission(
        read_permission,
    )

    admin_role.add_permission(
        write_permission,
    )

    service = (
        PermissionResolutionService()
    )

    permissions = service.resolve(
        roles=[admin_role],
    )

    assert len(permissions) == 2
