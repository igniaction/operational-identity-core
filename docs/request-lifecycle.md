# Request Lifecycle

---

# Overview

This document describes the complete operational lifecycle
of an HTTP request inside the Operational Identity Core.

---

# Flow

```mermaid
sequenceDiagram

    participant Client
    participant Flask
    participant UseCase
    participant Domain
    participant Repository
    participant PostgreSQL

    Client->>Flask: HTTP Request

    Flask->>UseCase: DTO

    UseCase->>Domain: Execute business rules

    UseCase->>Repository: Persist/Retrieve data

    Repository->>PostgreSQL: SQL operations

    PostgreSQL-->>Repository: persisted data

    Repository-->>UseCase: domain entity

    UseCase-->>Flask: result

    Flask-->>Client: HTTP Response
