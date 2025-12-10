def get_path(route):
    """
    Return the path of any route
    E.G.
    {
        "id": 294,
        "module": "ai",
        "function": "bin",
        ...
    }
    will return ai/bin
    """
    return "/".join([route["module"], route["function"]] + route["parameters"])

def get_parameter_doc(param: str, param_type: str, example: str):
    """
    Return the OpenAPI documentation of a leekwars api parameter
    """
    return {
        "name": param,
        "in": "path",
        "required": True,
        "schema": {
            "type": "integer" if param_type == "number" else param_type
        },
        "example": example
    }


def get_doc(route):
    examples = (route["example_url"] or "").split("/")
    return {
        "tags": [route["module"]],
        "parameters": [
            get_parameter_doc(route["parameters"][i], route["parameters_types"][i], examples[2 + i] if len(examples) > 2+i else None) for i in range(len(route["parameters"]))
        ]
    }


def get_method(route):
    return route["method"]


def route_converter(route):
    return get_path(route), get_method(route), get_doc(route)