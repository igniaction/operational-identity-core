"""
JWT payload assembly example.
"""

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


def main() -> None:
    """
    Assemble JWT-compatible payload.
    """

    permission_read = Permission(
        name="READ_REPORTS",
    )

    permission_write = Permission(
        name="WRITE_REPORTS",
    )

    manager_role = Role(
        name="MANAGER",
        permissions=[
            permission_read,
            permission_write,
        ],
    )

    user = User(
        email=Email(
            "manager@platform.io",
        ),
        username=Username(
            "manager",
        ),
    )

    service = (
        IdentityResolutionService()
    )

    context = service.resolve(
        user=user,
        roles=[manager_role],
    )

    jwt_payload = {
        "sub": str(context.user.id),
        "username": (
            context.user.username.value
        ),
        "roles": [
            role.name
            for role in context.roles
        ],
        "permissions": [
            permission.name
            for permission
            in context.permissions
        ],
    }

    print(
        "\nJWT-compatible payload:\n",
    )

    print(jwt_payload)


if __name__ == "__main__":
    main()
