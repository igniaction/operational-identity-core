"""
Create database tables.
"""

from operational_identity_core.infrastructure.persistence.database import (
    Base,
)

from operational_identity_core.infrastructure.persistence.database import (
    engine,
)

from operational_identity_core.infrastructure.persistence.permission_model import (
    PermissionModel,
)

from operational_identity_core.infrastructure.persistence.role_model import (
    RoleModel,
)

from operational_identity_core.infrastructure.persistence.role_permission_model import (
    RolePermissionModel,
)

from operational_identity_core.infrastructure.persistence.user_model import (
    UserModel,
)

from operational_identity_core.infrastructure.persistence.user_role_model import (
    UserRoleModel,
)


def main() -> None:
    """
    Create all tables.
    """

    _ = (
        UserModel,
        RoleModel,
        PermissionModel,
        UserRoleModel,
        RolePermissionModel,
    )

    Base.metadata.create_all(
        bind=engine,
    )


if __name__ == "__main__":
    main()
