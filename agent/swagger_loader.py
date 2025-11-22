import json
def load_swagger(path):
    with open(path,'r') as f: return json.load(f)
