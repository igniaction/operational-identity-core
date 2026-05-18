# Permission Aggregation

---

# Overview

Permission aggregation is executed through domain services.

The process intentionally remains independent from:

- HTTP runtimes
- JWT libraries
- ORM behavior

---

# Aggregation Process

```mermaid
flowchart TD

    Roles[Roles]

    Resolver[PermissionResolutionService]

    Permissions[Aggregated Permissions]

    Roles --> Resolver

    Resolver --> Permissions
