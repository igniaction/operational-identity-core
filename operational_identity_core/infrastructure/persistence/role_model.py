"""
SQLAlchemy role model.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from operational_identity_core.infrastructure.persistence.database import (
    Base,
)

from operational_identity_core.infrastructure.persistence.permission_model import (
    PermissionModel,
)

from operational_identity_core.infrastructure.persistence.role_permission_model import (
    RolePermissionModel,
)


class RoleModel(Base):
    """
    ORM role representation.
    """

    __tablename__ = "roles"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    permissions: Mapped[list[PermissionModel]] = (
        relationship(
            secondary=RolePermissionModel.__table__,
        )
    )
