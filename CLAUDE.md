# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Learning project demonstrating how to use LLMs to call REST APIs via function calling. The goal is to enable natural language queries like "what is my todo list for today" that the LLM understands and translates into one or more API calls.

The system loads Swagger/OpenAPI specs and converts them to OpenAI tool schemas, allowing the LLM to dynamically discover and call API endpoints.

## Commands

### Running Services
```bash
# Todo API (port 8001)
uvicorn todo_server.main:app --port 8001 --reload

# Agent API Gateway (port 8000)
uvicorn api_gateway.main:app --port 8000 --reload

# Docker Compose (runs both services)
docker-compose up
```

### Testing
```bash
pytest                    # Run all tests
pytest tests/test_agent.py  # Run specific test file
```

### Dependencies
```bash
pip install -r requirements.txt
```

## Architecture

### Two-Service Design
- **api_gateway** (port 8000): FastAPI service that exposes `/chat` endpoint, runs the agent loop
- **todo_server** (port 8001): FastAPI CRUD API for todos with SQLite database

### Agent Flow
1. `api_gateway/main.py` loads Swagger spec from `todo_server/swagger.json`
2. `agent/tool_schema_converter.py` converts OpenAPI paths to OpenAI function tool schemas
3. `agent/loop.py` runs the conversation loop, calling OpenAI and executing tools
4. `agent/tool_executor.py` translates tool calls back to HTTP requests to the todo server

### Tool Naming Convention
Tools are named as `{method}__{path}` where path segments become underscores:
- `GET /todos` → `get__todos`
- `POST /todos` → `post__todos`
- `GET /todos/{id}` → `get__todos_{id}`

### Environment
Requires `OPENAI_API_KEY` environment variable for the agent to function.
