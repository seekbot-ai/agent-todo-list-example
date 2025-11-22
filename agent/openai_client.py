import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def call_openai(messages, tools):
    response = await client.responses.create(
        model="gpt-4.1",
        input=messages,
        tools=tools,
        tool_choice="auto"
    )
    return response.output[0]
