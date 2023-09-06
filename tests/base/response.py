from jsonschema import validate

from tests.enums.errors import GlobalError


class Response:
    def __init__(self, response):
        self.response = response.json()
        self.status_code = response.status_code

    def validate(self, schema):
        if isinstance(self.response, list):
            for item in self.response:
                validate(item, schema)
        else:
            validate(self.response, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.status_code in status_code, GlobalError.WRONG_STATUS_CODE.value

    def assert_count_items(self, count):
        assert len(self.response) == 3, GlobalError.WRONG_NUMBER_OF_POSTS.value
