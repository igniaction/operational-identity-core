from uuid import uuid4

from operational_identity_core.application.use_cases.resolve_permissions_use_case import (
    ResolvePermissionsUseCase,
)

from operational_identity_core.domain.entities.permission import (
    Permission,
)

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.domain.repositories.role_repository import (
    RoleRepository,
)


class FakeRoleRepository(
    RoleRepository,
):

    def __init__(self) -> None:

        permission = Permission(
            name="READ_USERS",
        )

        role = Role(
            id=uuid4(),
            name="ADMIN",
            permissions=[permission],
        )

        self.roles = [role]

    def find_roles_by_user(
        self,
        user_id: str,
    ) -> list[Role]:

        return self.roles

    def save(
        self,
        role: Role,
    ) -> None:
        pass


def test_should_resolve_permissions() -> None:

    repository = (
        FakeRoleRepository()
    )

    use_case = (
        ResolvePermissionsUseCase(
            role_repository=repository,
        )
    )

    permissions = use_case.execute(
        user_id="123",
    )

    assert permissions == [
        "READ_USERS",
    ]
