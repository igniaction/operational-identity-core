from operational_identity_core.domain.entities.user import (
    User,
)

from operational_identity_core.domain.value_objects.email import (
    Email,
)

from operational_identity_core.domain.value_objects.username import (
    Username,
)

from operational_identity_core.domain.value_objects.identity_status import (
    IdentityStatus,
)


def test_should_activate_user() -> None:

    user = User(
        email=Email("admin@platform.io"),
        username=Username("admin"),
    )

    user.activate()

    assert user.status == IdentityStatus.ACTIVE
