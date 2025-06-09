# Architecture Overview

This project is a Python-based command line interface (CLI) application for deep research. The design is derived from the goals and features described in the README and focuses on combining multiple AI services with automated web data collection. Below is an outline of the core components and how they interact.

## Goals

* Collect information from the web for a user-provided research topic.
* Utilize various AI services to analyze, summarize and reason over the collected data.
* Produce citation-based summaries, while checking for accuracy and bias.
* Plan and organize research in logical sections that form a coherent report.

## High-Level Components

1. **CLI Entrypoint**
   - Implemented with the `typer` library for a modern command-line experience.
   - Accepts the research topic and options such as output format or depth of search.
   - Triggers the overall workflow.

2. **Web Crawler and Data Collector**
   - Uses `aiohttp` for asynchronous HTTP requests to gather webpages quickly.
   - Extracts relevant text and metadata from each page.
   - Saves raw content for later reference and citation.

3. **AI Service Connectors**
   - Modular interface supporting multiple providers (e.g. OpenAI GPT-4o or other LLM APIs).
   - Each connector implements a unified method for sending prompts and receiving responses.
   - Enables easy integration of new AI models as they become available.

4. **Summarization and Reasoning Engine**
   - Orchestrates calls to AI services to summarize website content and synthesize findings.
   - Plans the research sections, tracks logical implications, and generates a coherent narrative.
   - Leverages asynchronous calls to AI endpoints to keep the workflow responsive.
5. **Research Feedback Loop**
   - After each summary pass, the reasoning engine can request deeper coverage of a sub-topic.
   - The crawler performs targeted searches and feeds new data back into the workflow.


6. **Fact-Check and Bias-Check Modules**
   - Run collected information through separate AI models or heuristics to verify claims and identify bias.
   - Annotate summaries with notes on reliability or potential issues.

7. **Citation Manager**
   - Maintains references to all sources gathered by the crawler.
   - Associates citations with summary sections, ensuring traceability of each statement.

8. **Report Generator**
   - Combines summarized sections, citations, and verification notes into a final document.
   - Supports multiple formats (e.g. Markdown or PDF) for export.

## Data Flow

1. User runs the CLI command with a research topic.
2. The crawler gathers web pages relevant to the topic and stores the raw text.
3. The summarization engine sends content chunks to AI services for processing.
4. If more detail is required, the reasoning engine instructs the crawler to perform targeted searches for specific sub-topics.
5. Newly collected content re-enters the summarization and verification steps until sufficient coverage is reached.
6. Results are fact-checked, bias-checked, and then stored with their citations.
7. The report generator assembles all verified summaries into a complete research report.

## Modern Techniques

* **Asynchronous I/O** with `async`/`await` ensures efficient web scraping and API calls.
* **Type hints** and data models (e.g. `pydantic` or `dataclasses`) keep the codebase robust and maintainable.
* **Typer** provides a user-friendly CLI with minimal boilerplate.
* Modular design allows new AI services or analysis modules to be plugged in without rewriting the core workflow.
* **Iterative feedback loops** allow the AI to request more data from the crawler when summaries lack depth.

This architecture supports the repository's goal of delivering a citation-rich research assistant that plans and summarizes information beyond typical LLM capabilities.

