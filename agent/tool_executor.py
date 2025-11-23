import httpx
import json

API="http://localhost:8001"

async def execute_tool(name,args):
    method, path = name.split("__",1)
    url=f"{API}/{path.replace('_','/')}"
    m=method.upper()

    # Parse args if it's a string
    if isinstance(args, str):
        args = json.loads(args) if args else {}

    async with httpx.AsyncClient() as c:
        if m=="GET":
            r=await c.get(url, params=args)
        else:
            r=await c.request(m, url, json=args)
        # Return as JSON string for tool message content
        return json.dumps(r.json())
