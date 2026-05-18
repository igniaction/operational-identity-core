"""
Create user use case.
"""

from operational_identity_core.application.dto.create_user_dto import (
    CreateUserDTO,
)

from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.repositories.user_repository import (
    UserRepository,
)

from operational_identity_core.domain.value_objects.email import (
    Email,
)

from operational_identity_core.domain.value_objects.username import (
    Username,
)

from operational_identity_core.infrastructure.logging.runtime_logger import (
    logger,
)


class CreateUserUseCase:
    """
    Create operational identity.
    """

    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:

        self.user_repository = (
            user_repository
        )

    def execute(
        self,
        dto: CreateUserDTO,
    ) -> User:
        """
        Execute user creation.
        """

        logger.info(
            "USER_CREATION started username=%s",
            dto.username,
        )

        user = User(
            email=Email(dto.email),
            username=Username(dto.username),
        )

        self.user_repository.save(
            user,
        )

        logger.info(
            "USER_CREATED id=%s username=%s",
            user.id,
            user.username.value,
        )

        return user
