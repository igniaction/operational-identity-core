"""
Username value object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Username:
    """
    Immutable username representation.
    """

    value: str

    def __post_init__(self) -> None:

        if len(self.value.strip()) < 3:
            raise ValueError("Username too short.")

    def __str__(self) -> str:
        return self.value
