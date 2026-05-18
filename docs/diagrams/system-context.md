# System Context Diagram

```mermaid
flowchart TD

    Developer[Developer]
    CLI[CLI Runtime]
    Flask[Flask Runtime]
    JWT[JWT Payload Runtime]

    IdentityCore[Operational Identity Core]

    PostgreSQL[(PostgreSQL)]

    Developer --> CLI
    Developer --> Flask

    CLI --> IdentityCore
    Flask --> IdentityCore
    JWT --> IdentityCore

    IdentityCore --> PostgreSQL
