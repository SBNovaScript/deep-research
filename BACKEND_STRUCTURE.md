# Planned Backend Directory Layout

This repository contains a Python-based API within a `backend/` folder. The structure below organizes endpoints, business logic, and resources so each concern remains modular.

```
backend/
  app/
    api/          # FastAPI route handlers
    models/       # Pydantic models and database schemas
    services/     # Core business logic
    utils/        # Shared helper functions
  config/         # Application settings and environment files
  data/           # Local cache and scraped website content
  tests/          # Automated tests for the backend API
```

Additional submodules can be added to `app/` or `config/` as the project grows (for example, new service layers or logging utilities).
