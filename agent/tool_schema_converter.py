def swagger_to_tools(spec):
    tools=[]
    for path, methods in spec.get("paths",{}).items():
        clean=path.strip("/")
        for method,info in methods.items():
            name=f"{method}__{clean.replace('/','_')}"
            schema={"type":"object","properties":{}, "required":[]}

            for p in info.get("parameters",[]):
                pname=p["name"]
                schema["properties"][pname]={"type":p["schema"]["type"]}
                if p.get("required"): schema["required"].append(pname)

            if "requestBody" in info:
                body=info["requestBody"]["content"]["application/json"]["schema"]
                schema["properties"].update(body.get("properties",{}))
                schema["required"]+=body.get("required",[])

            tools.append({
                "type":"function",
                "function":{
                    "name":name,
                    "description": info.get("summary", f"{method} {path}"),
                    "parameters": schema
                }
            })
    return tools
