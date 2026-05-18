"""
SQLAlchemy role repository.
"""

from sqlalchemy.orm import Session

from operational_identity_core.domain.entities.role import (
    Role,
)

from operational_identity_core.domain.repositories.role_repository import (
    RoleRepository,
)

from operational_identity_core.infrastructure.mappers.role_mapper import (
    RoleMapper,
)

from operational_identity_core.infrastructure.persistence.user_model import (
    UserModel,
)


class SQLAlchemyRoleRepository(
    RoleRepository,
):
    """
    SQLAlchemy role repository.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        self.session = session

    def find_roles_by_user(
        self,
        user_id: str,
    ) -> list[Role]:

        user = (
            self.session.query(UserModel)
            .filter_by(id=user_id)
            .first()
        )

        if user is None:
            return []

        return [
            RoleMapper.to_domain(role)
            for role in user.roles
        ]

    def save(
        self,
        role: Role,
    ) -> None:

        model = RoleMapper.to_model(
            role,
        )

        self.session.add(model)

        self.session.commit()
