"""
Role permission association model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from operational_identity_core.infrastructure.persistence.database import (
    Base,
)


class RolePermissionModel(Base):
    """
    Role permission association.
    """

    __tablename__ = "role_permissions"

    role_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("roles.id"),
        primary_key=True,
    )

    permission_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("permissions.id"),
        primary_key=True,
    )
