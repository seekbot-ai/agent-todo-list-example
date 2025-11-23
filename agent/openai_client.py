import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a helpful assistant that manages a todo list through API calls.

You have access to these tools:
- get__todos: List all todos
- post__todos: Create a new todo
- get__todos_id: Get a specific todo by ID
- put__todos_id: Update a todo by ID
- delete__todos_id: Delete a todo by ID

IMPORTANT: When a user refers to a todo by its title (not ID), you MUST:
1. First call get__todos to list all todos and find the matching ID
2. Then use that ID to perform the requested operation (update, delete, etc.)

Always complete multi-step tasks by calling multiple tools as needed."""

async def call_openai(messages, tools):
    # Convert string messages to proper format
    formatted_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in messages:
        if isinstance(msg, str):
            formatted_messages.append({"role": "user", "content": msg})
        else:
            formatted_messages.append(msg)

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=formatted_messages,
        tools=tools,
        tool_choice="auto"
    )
    return response.choices[0].message
