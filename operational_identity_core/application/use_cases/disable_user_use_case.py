"""
Disable user use case.
"""

from operational_identity_core.domain.repositories.user_repository import (
    UserRepository,
)


class DisableUserUseCase:
    """
    Disable operational identity.
    """

    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:

        self.user_repository = user_repository

    def execute(
        self,
        username: str,
    ) -> None:
        """
        Disable user.
        """

        user = (
            self.user_repository.find_by_username(
                username,
            )
        )

        if user is None:
            raise ValueError("User not found.")

        user.disable()

        self.user_repository.save(user)
