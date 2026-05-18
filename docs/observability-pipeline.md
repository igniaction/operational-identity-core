# Observability Pipeline

---

# Overview

Operational Identity Core includes runtime observability
through structured execution logs.

---

# Observability Flow

```mermaid
flowchart TD

    Runtime[Runtime Adapter]

    UseCase[Use Case]

    Domain[Domain Service]

    Logger[Operational Logger]

    Runtime --> UseCase

    UseCase --> Domain

    Domain --> Logger
