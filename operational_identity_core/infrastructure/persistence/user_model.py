"""
SQLAlchemy user model.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from operational_identity_core.infrastructure.persistence.database import (
    Base,
)

from operational_identity_core.infrastructure.persistence.role_model import (
    RoleModel,
)

from operational_identity_core.infrastructure.persistence.user_role_model import (
    UserRoleModel,
)


class UserModel(Base):
    """
    ORM user representation.
    """

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    username: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    roles: Mapped[list[RoleModel]] = (
        relationship(
            secondary=UserRoleModel.__table__,
        )
    )
