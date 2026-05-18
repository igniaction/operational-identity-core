# Container View Diagram

```mermaid
flowchart TD

    FlaskAdapter[Flask Adapter]
    CLIRuntime[CLI Runtime]
    JWTRuntime[JWT Runtime]

    ApplicationLayer[Application Layer]

    DomainLayer[Domain Layer]

    InfrastructureLayer[Infrastructure Layer]

    PostgreSQL[(PostgreSQL)]

    FlaskAdapter --> ApplicationLayer
    CLIRuntime --> ApplicationLayer
    JWTRuntime --> ApplicationLayer

    ApplicationLayer --> DomainLayer

    ApplicationLayer --> InfrastructureLayer

    InfrastructureLayer --> PostgreSQL
