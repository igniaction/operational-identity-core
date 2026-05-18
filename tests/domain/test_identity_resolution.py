from operational_identity_core.domain.entities.permission import (
    Permission,
)

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.services.identity_resolution_service import (
    IdentityResolutionService,
)

from operational_identity_core.domain.value_objects.email import (
    Email,
)

from operational_identity_core.domain.value_objects.username import (
    Username,
)


def test_should_resolve_identity_context() -> None:

    permission = Permission(
        name="READ_REPORTS",
    )

    role = Role(
        name="MANAGER",
    )

    role.add_permission(permission)

    user = User(
        email=Email("manager@platform.io"),
        username=Username("manager"),
    )

    service = IdentityResolutionService()

    context = service.resolve(
        user=user,
        roles=[role],
    )

    assert context.user.username.value == "manager"

    assert len(context.permissions) == 1

    assert context.permissions[0].name == (
        "READ_REPORTS"
    )
