"""
Identity activation service.
"""

from operational_identity_core.domain.entities.user import (
    User,
)


class IdentityActivationService:
    """
    Handle operational identity activation.
    """

    def activate(
        self,
        user: User,
    ) -> None:
        """
        Activate operational identity.
        """

        user.activate()

    def disable(
        self,
        user: User,
    ) -> None:
        """
        Disable operational identity.
        """

        user.disable()
