install:
	pip install -e .[dev]

test:
	pytest

lint:
	ruff check .

typecheck:
	mypy operational_identity_core

run-cli:
	python -m examples.cli_runtime.main

run-flask:
	python -m examples.flask_integration.app

run-jwt:
	python -m examples.jwt_payload_assembly.example

create-tables:
	python scripts/create_tables.py

migration:
	alembic revision --autogenerate -m "$(m)"

upgrade:
	alembic upgrade head

docker-up:
	docker compose up -d

docker-down:
	docker compose down
