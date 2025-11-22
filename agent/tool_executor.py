import httpx
API="http://localhost:8001"

async def execute_tool(name,args):
    method, path = name.split("__",1)
    url=f"{API}/{path.replace('_','/')}"
    m=method.upper()

    async with httpx.AsyncClient() as c:
        if m=="GET":
            r=await c.get(url, params=args)
        else:
            r=await c.request(m, url, json=args)
        return r.json()
