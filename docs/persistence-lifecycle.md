# Persistence Lifecycle

---

# Overview

Persistence is implemented through repository abstractions
and SQLAlchemy adapters.

The domain layer never directly manipulates ORM models.

---

# Persistence Flow

```mermaid
sequenceDiagram

    participant UseCase
    participant Repository
    participant Mapper
    participant SQLAlchemy
    participant PostgreSQL

    UseCase->>Repository: Domain Entity

    Repository->>Mapper: Map Entity

    Mapper->>SQLAlchemy: ORM Model

    SQLAlchemy->>PostgreSQL: SQL Persistence
