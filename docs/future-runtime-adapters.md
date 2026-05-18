# Future Runtime Adapters

---

# Current Adapters

| Adapter | Status |
|---|---|
| Flask | implemented |
| CLI | implemented |
| JWT Assembly | implemented |
| Docker Runtime | implemented |

---

# Planned Adapters

| Adapter | Purpose |
|---|---|
| FastAPI | async HTTP runtime |
| gRPC | service-to-service communication |
| GraphQL | flexible querying |
| Event Runtime | distributed capability propagation |

---

# Architectural Principle

Adapters must remain replaceable.

The domain layer should never depend directly on runtime
implementations.
