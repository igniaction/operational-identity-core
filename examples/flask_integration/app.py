"""
Flask integration example.
"""

from flask import Flask
from flask import jsonify
from flask import request

from operational_identity_core.application.dto.create_user_dto import (
    CreateUserDTO,
)

from operational_identity_core.application.use_cases.create_user_use_case import (
    CreateUserUseCase,
)

from examples.shared.fake_user_repository import (
    FakeUserRepository,
)


app = Flask(__name__)

repository = (
    FakeUserRepository()
)

create_user_use_case = (
    CreateUserUseCase(
        user_repository=repository,
    )
)


@app.route(
    "/health",
    methods=["GET"],
)
def health() -> tuple[dict[str, str], int]:
    """
    Health endpoint.
    """

    return {
        "status": "healthy",
    }, 200


@app.route(
    "/users",
    methods=["POST"],
)
def create_user() -> tuple[dict, int]:
    """
    Create operational identity.
    """

    payload = request.get_json()

    if payload is None:

        return {
            "error": "Invalid payload.",
        }, 400

    dto = CreateUserDTO(
        email=payload["email"],
        username=payload["username"],
    )

    user = (
        create_user_use_case.execute(
            dto,
        )
    )

    return jsonify(
        {
            "id": str(user.id),
            "email": user.email.value,
            "username": user.username.value,
            "status": user.status.value,
        }
    ), 201


if __name__ == "__main__":

    app.run(
	host="0.0.0.0",
        debug=True,
        port=5000,
    )
