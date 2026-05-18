"""
Identity status value object.
"""

from enum import Enum


class IdentityStatus(str, Enum):
    """
    Identity operational status.
    """

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    PENDING = "PENDING"
