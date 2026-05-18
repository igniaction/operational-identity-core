"""
Identity context DTO.
"""

from dataclasses import dataclass


@dataclass
class IdentityContextDTO:
    """
    Operational identity context output.
    """

    user_id: str

    username: str

    permissions: list[str]
