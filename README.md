# Universal API Agent + Todo REST API

Full stack: FastAPI + OpenAI + Dynamic Swagger Tool Calling + React Frontend.

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 20.19+ or 22.12+
- [uv](https://github.com/astral-sh/uv) (Python package manager)

### Installation

```bash
# Clone the repository
git clone git@github.com:seekbot-ai/agent-todo-list-example.git
cd agent-todo-list-example

# Install Python dependencies
uv sync

# Install frontend dependencies
cd frontend
npm install
cd ..
```

### Running Locally

#### 1. Start the Todo API (Backend)

```bash
uv run uvicorn todo_server.main:app --port 8001 --reload
```

API available at http://localhost:8001
- Docs: http://localhost:8001/docs

#### 2. Start the React Frontend

```bash
cd frontend
npm run dev
```

Frontend available at http://localhost:5173

#### 3. Start the Agent API (Optional)

Requires `OPENAI_API_KEY` environment variable.

```bash
export OPENAI_API_KEY="your-key-here"
uv run uvicorn api_gateway.main:app --port 8000 --reload
```

Agent API available at http://localhost:8000

### Docker Compose

```bash
docker-compose up
```

## API Endpoints

### Todo Server (port 8001)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /todos | List all todos |
| GET | /todos/{id} | Get a todo |
| POST | /todos | Create a todo |
| PUT | /todos/{id} | Update a todo |
| DELETE | /todos/{id} | Delete a todo |

### Agent API (port 8000)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /chat | Chat with the AI agent |

## Testing

```bash
uv run pytest
```
