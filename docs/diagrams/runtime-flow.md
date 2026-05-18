# Runtime Flow Diagram

```mermaid
sequenceDiagram

    participant Client
    participant Flask
    participant UseCase
    participant Domain
    participant Repository
    participant PostgreSQL

    Client->>Flask: HTTP POST /users

    Flask->>UseCase: CreateUserDTO

    UseCase->>Domain: Create User Entity

    UseCase->>Repository: Persist User

    Repository->>PostgreSQL: INSERT user

    PostgreSQL-->>Repository: persisted

    Repository-->>UseCase: User

    UseCase-->>Flask: User

    Flask-->>Client: JSON Response
