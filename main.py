import json

from route_converter import route_converter

with open("template.json") as template:
    out_doc = json.load(template)

# Read the input doc obtained from https://leekwars.com/api/service/get-all
with open("input.json") as input_doc:
    for route in json.load(input_doc):
        path, method, doc = route_converter(route)
        if path not in out_doc["paths"]:
            out_doc["paths"][path] = {}

        out_doc["paths"][path][method] = doc

with open("output.json", 'w') as output:
    output.write(json.dumps(out_doc, indent=2))