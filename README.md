# Deep Research

This repository contains a custom deep research implementation designed to connect to multiple AI services. It collects data from the web based on a user-provided research topic, analyzes the information with diverse AI models, and produces citation-driven summaries. The system is intended to build a coherent research report that goes beyond normal LLM limitations by planning and summarizing each section strategically.

This repository is structured as a monorepo containing both a web frontend and a backend API. The `frontend` directory hosts the user interface, while the `backend` directory handles data collection and AI processing. These components work together to provide an integrated research assistant.


## Features

- Integration with various AI services (e.g. OpenAI GPT-4o) for summarization and reasoning
- Website scanning to gather data relevant to a research request
- Fact-check and bias-check modules to ensure accurate and balanced summaries
- Centralized prompt templates defining instructions for each AI task
- Expansive research planning that links logical implications across sources
- Comprehensive, citation-rich reports for any topic
- Web-based interface for launching research tasks and viewing reports
- Backend API orchestrates data collection and summarization
- Configurable backend endpoint via `.env` using Vite's environment variables

This project is in an early stage. Future updates will include plug-in submodules for source validation, bias detection, and more automated workflows.

## Frontend Development

The `frontend` folder contains a minimal React application built with Vite and Tailwind CSS. To run it locally:

```bash
cd frontend
npm install
npm run dev
```

This will start a development server at <http://localhost:5173>.

The frontend uses React Router v7's data router API via the `react-router` package. Our
routes are configured with `createBrowserRouter` and rendered by `RouterProvider`.

=======
### Configuring API Endpoint

Vite exposes environment variables that start with `RESEARCH_` via
`import.meta.env`. Copy `.env.example` in the `frontend` directory to `.env`
and update the variables for your environment:

```bash
cd frontend
cp .env.example .env
# edit .env to point to your backend
```

The frontend uses `RESEARCH_API_URL` to determine where requests to the backend
should be sent.

## Backend Development

The backend uses [uv](https://github.com/astral-sh/uv) for dependency
management. `uv` is a fast drop-in replacement for the standard `pip` tooling
that supports lockfiles and reproducible resolutions. From the `backend`
directory install the requirements with:

```bash
cd backend
uv pip install -r requirements.txt
```

To generate a lockfile and install from it later run:

```bash
uv lock
uv sync
```

Set the `OPENAI_API_KEY` environment variable so the backend can authenticate
with OpenAI:

```bash
export OPENAI_API_KEY=your_key_here
```

Then start the API with:

```bash
uvicorn app.main:app --reload
```
