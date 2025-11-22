from fastapi import FastAPI, Body
from agent.loop import run_agent
from agent.swagger_loader import load_swagger
from agent.tool_schema_converter import swagger_to_tools

app=FastAPI(title="AI Gateway")

swagger=load_swagger("todo_server/swagger.json")
tools=swagger_to_tools(swagger)

@app.post("/chat")
async def chat(messages:list=Body(...)):
    return {"reply": await run_agent(messages, tools)}
