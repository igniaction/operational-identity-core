from uuid import uuid4

from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.value_objects.email import (
    Email,
)

from operational_identity_core.domain.value_objects.username import (
    Username,
)

from operational_identity_core.infrastructure.persistence.database import (
    SessionLocal,
)

from operational_identity_core.infrastructure.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)


def test_should_persist_user() -> None:

    session = SessionLocal()

    repository = (
        SQLAlchemyUserRepository(
            session=session,
        )
    )

    unique_id = str(uuid4())[:8]

    user = User(
        email=Email(
            f"{unique_id}@test.com",
        ),
        username=Username(
            f"user_{unique_id}",
        ),
    )

    repository.save(user)

    persisted = (
        repository.find_by_username(
            user.username.value,
        )
    )

    assert persisted is not None
