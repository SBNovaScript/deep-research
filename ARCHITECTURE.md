# Architecture Overview

This repository is organized as a monorepo that houses both a backend service and a frontend application. The backend is implemented in Python and exposes an API that streams research results directly to the browser. The design is derived from the goals and features described in the README and focuses on combining multiple AI services with automated web data collection. The React-based frontend presents these results in a user-friendly way. Below is an outline of the core components and how they interact.

### Repository Layout

```
/backend   # Python API server that streams results to the frontend
/frontend  # React + TypeScript + Tailwind web application
```

## Goals

* Collect information from the web for a user-provided research topic.
* Utilize various AI services to analyze, summarize and reason over the collected data.
* Produce citation-based summaries, while checking for accuracy and bias.
* Plan and organize research in logical sections that form a coherent report.

## High-Level Components

1. **Backend Service**
   - Implemented in Python as an API server.
   - Streams progress and final summaries to the frontend for real-time updates.
   - Coordinates the overall workflow described below.

2. **Frontend Web Application**
   - Built with React, TypeScript and styled with Tailwind CSS.
   - Allows users to submit research requests and view results in the browser.
   - Receives streamed data from the backend API for seamless interaction.
3. **Web Crawler and Data Collector**
   - Uses `aiohttp` for asynchronous HTTP requests to gather webpages quickly.
   - Extracts relevant text and metadata from each page.
   - Saves raw content for later reference and citation.

4. **AI Service Connectors**
   - Modular interface supporting multiple providers (e.g. OpenAI GPT-4o or other LLM APIs).
   - Each connector implements a unified method for sending prompts and receiving responses.
   - Enables easy integration of new AI models as they become available.
5. **Prompt Templates**
   - Centralized module defining the instructions used by AI services.
   - Includes prompts for summarization, fact checking, and bias detection.
   - Keeps the workflow consistent and makes it easy to adjust system behavior.

6. **Summarization and Reasoning Engine**
   - Orchestrates calls to AI services to summarize website content and synthesize findings.
   - Plans the research sections, tracks logical implications, and generates a coherent narrative.
   - Leverages asynchronous calls to AI endpoints to keep the workflow responsive.
7. **Research Feedback Loop**
   - After each summary pass, the reasoning engine can request deeper coverage of a sub-topic.
   - The crawler performs targeted searches and feeds new data back into the workflow.

8. **Fact-Check and Bias-Check Modules**
   - Run collected information through separate AI models or heuristics to verify claims and identify bias.
   - Annotate summaries with notes on reliability or potential issues.

9. **Citation Manager**
   - Maintains references to all sources gathered by the crawler.
   - Associates citations with summary sections, ensuring traceability of each statement.

10. **Report Generator**
   - Combines summarized sections, citations, and verification notes into a final document.
   - Supports multiple formats (e.g. Markdown or PDF) for export.

## Data Flow

1. A user submits a research topic through the React frontend.
2. The frontend sends the request to the backend API and begins receiving streamed updates.
3. The crawler gathers web pages relevant to the topic and stores the raw text.
4. The summarization engine sends content chunks to AI services for processing.
5. If more detail is required, the reasoning engine instructs the crawler to perform targeted searches for specific sub-topics.
6. Newly collected content re-enters the summarization and verification steps until sufficient coverage is reached.
7. Results are fact-checked, bias-checked, and then stored with their citations.
8. The report generator assembles all verified summaries into a complete research report.

## Modern Techniques

* **Asynchronous I/O** with `async`/`await` ensures efficient web scraping and API calls.
* **Type hints** and data models (e.g. `pydantic` or `dataclasses`) keep the codebase robust and maintainable.
* Modular design allows new AI services or analysis modules to be plugged in without rewriting the core workflow.
* **Streaming** updates keep the frontend synchronized with backend progress.
* **Iterative feedback loops** allow the AI to request more data from the crawler when summaries lack depth.

This architecture supports the repository's goal of delivering a citation-rich research assistant that plans and summarizes information beyond typical LLM capabilities.

