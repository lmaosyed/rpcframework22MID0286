import json
from marshalling import validate_types

class RPCServer:
    def __init__(self):
        self.methods = {}

    def register_method(self, name, func, schema):
        self.methods[name] = (func, schema)

    def handle_request(self, request_json):
        request = json.loads(request_json)
        method = request["method"]
        params = request["params"]

        if method not in self.methods:
            raise Exception("Method not found")

        func, schema = self.methods[method]

        validate_types(params, schema)

        result = func(params)
        return json.dumps({"result": result})
