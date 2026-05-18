from operational_identity_core.application.dto.create_user_dto import (
    CreateUserDTO,
)

from operational_identity_core.application.use_cases.create_user_use_case import (
    CreateUserUseCase,
)

from operational_identity_core.application.use_cases.disable_user_use_case import (
    DisableUserUseCase,
)

from operational_identity_core.domain.value_objects.identity_status import (
    IdentityStatus,
)

from examples.shared.fake_user_repository import (
    FakeUserRepository,
)


def test_should_disable_user() -> None:

    repository = FakeUserRepository()

    create_use_case = (
        CreateUserUseCase(
            user_repository=repository,
        )
    )

    create_use_case.execute(
        CreateUserDTO(
            email="admin@platform.io",
            username="admin",
        )
    )

    disable_use_case = (
        DisableUserUseCase(
            user_repository=repository,
        )
    )

    disable_use_case.execute(
        username="admin",
    )

    user = repository.find_by_username(
        "admin",
    )

    assert user is not None

    assert user.status == (
        IdentityStatus.DISABLED
    )
