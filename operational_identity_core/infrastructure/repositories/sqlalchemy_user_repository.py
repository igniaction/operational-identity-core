"""
SQLAlchemy user repository.
"""

from sqlalchemy.orm import Session

from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.repositories.user_repository import (
    UserRepository,
)

from operational_identity_core.infrastructure.mappers.user_mapper import (
    UserMapper,
)

from operational_identity_core.infrastructure.persistence.user_model import (
    UserModel,
)


class SQLAlchemyUserRepository(
    UserRepository,
):
    """
    SQLAlchemy repository implementation.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        self.session = session

    def save(
        self,
        user: User,
    ) -> None:

        existing = self.session.get(
            UserModel,
            str(user.id),
        )

        if existing is None:

            model = (
                UserMapper.to_model(user)
            )

            self.session.add(model)

        self.session.commit()

    def find_by_username(
        self,
        username: str,
    ) -> User | None:

        model = (
            self.session.query(UserModel)
            .filter_by(username=username)
            .first()
        )

        if model is None:
            return None

        return UserMapper.to_domain(model)
