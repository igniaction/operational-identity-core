"""
CLI runtime example.
"""

from operational_identity_core.application.dto.create_user_dto import (
    CreateUserDTO,
)

from operational_identity_core.application.use_cases.create_user_use_case import (
    CreateUserUseCase,
)

from examples.shared.fake_user_repository import (
    FakeUserRepository,
)


def main() -> None:
    """
    Execute operational flow.
    """

    repository = (
        FakeUserRepository()
    )

    use_case = (
        CreateUserUseCase(
            user_repository=repository,
        )
    )

    user = use_case.execute(
        CreateUserDTO(
            email="cli@test.com",
            username="cli_user",
        )
    )

    print(
        "\nOperational identity created:",
    )

    print(
        f"ID: {user.id}",
    )

    print(
        f"Username: {user.username.value}",
    )


if __name__ == "__main__":
    main()
