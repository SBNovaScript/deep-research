# Frontend and Backend Entry Points

This document outlines the main HTTP routes that connect the React frontend with the Python backend service. The backend exposes a small REST/streaming API that the frontend uses to create research requests and receive live updates.

## POST `/api/research`
- **Description:** Start a new research task.
- **Payload:** JSON object containing a `topic` string and optional configuration values (e.g. depth, preferred sources).
- **Response:** JSON object with a generated `id` for tracking the research task.

Once the request is accepted, the backend immediately begins crawling websites and analyzing data.

## WebSocket `/ws/research/<id>`
- **Description:** Connect via WebSocket to receive progress updates for a research task.
- **Protocol:** Standard WebSocket that sends JSON messages as the backend gathers data and produces summaries.
- **Usage:** The React frontend opens a WebSocket to this route to display real-time status and intermediate results.

### Message Format

Each WebSocket message is a JSON object with a `type` field describing the
payload. Additional fields depend on the message category:

- `thinking` – AI reasoning or status updates.
  - `text` – content of the message.
- `search` – the system is fetching a URL.
  - `url` – address being visited.
- `citation` – a page has been stored for later citation.
  - `url` – source location.
- `final` – the completed report.
  - `text` – full summary text.

Example messages:

```json
{ "type": "thinking", "text": "Generating search queries" }
{ "type": "search", "url": "https://example.com" }
{ "type": "citation", "url": "https://example.com" }
{ "type": "final", "text": "<full report>" }
```

## GET `/api/research/<id>`
- **Description:** Retrieve the final consolidated research report.
- **Response:** JSON object containing the completed summary, citations, and metadata.

## Additional Endpoints
- **GET `/api/health`** – Simple health check used by the frontend to verify that the backend API is online.
- **Static assets** served by the frontend framework are delivered through the web server's root route (`/`).

These entrypoints provide a minimal yet flexible interface between the web application and the research engine running on the server. Frontend components can start new tasks, subscribe to streaming updates, and fetch the final report when processing is complete.
