# Universal API Agent + Todo REST API
Full stack: FastAPI + OpenAI Responses API + Dynamic Swagger Tool Calling + Devcontainer + Docker Compose.

Run:
- Todo API: uvicorn todo_server.main:app --port 8001 --reload
- Agent API: uvicorn api_gateway.main:app --port 8000 --reload
