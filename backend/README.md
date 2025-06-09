# Backend API

This directory contains the FastAPI application that powers the research engine. The service
crawls the web, summarizes pages with OpenAI models and compiles a report that can
be streamed to the frontend.

## Directory Layout

```
backend/
  app/
    api/          # FastAPI route handlers
    models/       # Pydantic request/response objects
    services/     # Core research logic
    utils/        # Helper utilities
  config/         # Application settings
  data/           # Cached pages and citations
  tests/          # Automated tests
```

## Installing Dependencies

The backend uses [uv](https://github.com/astral-sh/uv) for dependency
management. From this directory run:

```bash
uv pip install -r requirements.txt
```

To generate a lockfile and install from it later:

```bash
uv lock
uv sync
```

## Environment Variables

Set the following variables so the API can access external services:

```bash
export OPENAI_API_KEY=your_openai_key
export GOOGLE_API_KEY=your_google_api_key
export GOOGLE_CSE_ID=your_search_engine_id
```

## Running the Server

Start the development server with:

```bash
uvicorn app.main:app --reload
```

The API exposes routes described in `ENTRYPOINTS.md`, including a POST `/api/research`
endpoint and a WebSocket for streaming progress.

## Tests

Run the unit tests with:

```bash
pytest
```
