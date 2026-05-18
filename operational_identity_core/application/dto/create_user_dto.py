"""
Create user DTO.
"""

from dataclasses import dataclass


@dataclass
class CreateUserDTO:
    """
    User creation input data.
    """

    email: str

    username: str
