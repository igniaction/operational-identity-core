# Identity Propagation

---

# Overview

Identity propagation represents the process of transforming
organizational structures into operational context.

---

# Propagation Flow

```mermaid
flowchart TD

    User[User]

    Role[Role]

    Permission[Permission]

    Context[IdentityContext]

    User --> Role

    Role --> Permission

    Permission --> Context
