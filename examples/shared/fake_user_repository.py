from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.repositories.user_repository import (
    UserRepository,
)


class FakeUserRepository(
    UserRepository,
):

    def __init__(self) -> None:

        self.users: list[User] = []

    def save(
        self,
        user: User,
    ) -> None:

        existing = self.find_by_username(
            user.username.value,
        )

        if existing is None:
            self.users.append(user)

    def find_by_username(
        self,
        username: str,
    ) -> User | None:

        for user in self.users:

            if user.username.value == username:
                return user

        return None
