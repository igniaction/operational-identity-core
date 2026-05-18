"""
Email value object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    """
    Immutable email representation.
    """

    value: str

    def __post_init__(self) -> None:
        """
        Validate email structure.
        """

        if "@" not in self.value:
            raise ValueError("Invalid email address.")

        if "." not in self.value:
            raise ValueError("Invalid email domain.")

    def __str__(self) -> str:
        return self.value
