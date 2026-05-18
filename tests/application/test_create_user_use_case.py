from operational_identity_core.application.dto.create_user_dto import (
    CreateUserDTO,
)

from operational_identity_core.application.use_cases.create_user_use_case import (
    CreateUserUseCase,
)

from examples.shared.fake_user_repository import (
    FakeUserRepository,
)


def test_should_create_user() -> None:

    repository = FakeUserRepository()

    use_case = CreateUserUseCase(
        user_repository=repository,
    )

    dto = CreateUserDTO(
        email="admin@platform.io",
        username="admin",
    )

    user = use_case.execute(dto)

    assert user.username.value == "admin"

    assert len(repository.users) == 1
