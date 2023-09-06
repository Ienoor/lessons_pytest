from jsonschema import validate


class Response:
    def __init__(self, response, schema):
        self.response = response
        self.schema = schema

    def validate(self):
        if isinstance(self.response, list):
            for item in self.response:
                validate(item, self.schema)
        else:
            validate(self.response, self.schema)
