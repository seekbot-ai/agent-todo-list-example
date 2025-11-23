from .openai_client import call_openai
from .tool_executor import execute_tool

async def run_agent(messages, tools):
    while True:
        ai_msg = await call_openai(messages, tools)

        if ai_msg.tool_calls:
            # Add assistant message with tool calls
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [
                    {
                        "id": call.id,
                        "type": "function",
                        "function": {
                            "name": call.function.name,
                            "arguments": call.function.arguments
                        }
                    }
                    for call in ai_msg.tool_calls
                ]
            })

            for call in ai_msg.tool_calls:
                name = call.function.name
                args = call.function.arguments
                result = await execute_tool(name, args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result
                })
            continue

        return ai_msg.content
