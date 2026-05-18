"""
User mapper.
"""

from uuid import UUID

from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.value_objects.email import (
    Email,
)

from operational_identity_core.domain.value_objects.identity_status import (
    IdentityStatus,
)

from operational_identity_core.domain.value_objects.username import (
    Username,
)

from operational_identity_core.infrastructure.persistence.user_model import (
    UserModel,
)


class UserMapper:
    """
    Translate ORM <-> Domain.
    """

    @staticmethod
    def to_domain(
        model: UserModel,
    ) -> User:

        return User(
            id=UUID(model.id),
            email=Email(model.email),
            username=Username(model.username),
            status=IdentityStatus(model.status),
        )

    @staticmethod
    def to_model(
        entity: User,
    ) -> UserModel:

        return UserModel(
            id=str(entity.id),
            email=entity.email.value,
            username=entity.username.value,
            status=entity.status.value,
        )
