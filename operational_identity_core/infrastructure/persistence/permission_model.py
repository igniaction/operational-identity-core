"""
SQLAlchemy permission model.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from operational_identity_core.infrastructure.persistence.database import (
    Base,
)


class PermissionModel(Base):
    """
    ORM permission representation.
    """

    __tablename__ = "permissions"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
