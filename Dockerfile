FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -e .[dev]

EXPOSE 5000

CMD ["python", "-m", "examples.flask_integration.app"]
