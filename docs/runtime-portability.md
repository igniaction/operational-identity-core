# Runtime Portability

---

# Overview

The capability core was intentionally designed to operate
across multiple runtimes.

---

# Supported Runtimes

| Runtime | Purpose |
|---|---|
| CLI | operational execution |
| Flask | HTTP exposure |
| JWT Assembly | identity serialization |
| Docker | environment portability |

---

# Runtime Strategy

Adapters communicate with the application layer while the
domain remains isolated from runtime concerns.

---

# Architectural Goal

The operational capability must survive framework replacement
without requiring domain rewrites.
