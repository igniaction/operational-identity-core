"""
User role association model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from operational_identity_core.infrastructure.persistence.database import (
    Base,
)


class UserRoleModel(Base):
    """
    User role association.
    """

    __tablename__ = "user_roles"

    user_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("users.id"),
        primary_key=True,
    )

    role_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("roles.id"),
        primary_key=True,
    )
