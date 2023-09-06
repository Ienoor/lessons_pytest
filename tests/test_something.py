# https://my-json-server.typicode.com/typicode/demo/posts
import requests

from config import SERVICE_URL
from tests.base.response import Response
from tests.enums.errors import GlobalError
from tests.schemas.Posts import POST_SCHEMA

response = requests.get(SERVICE_URL)


def test_getting_status_code():
    assert response.status_code == 200, GlobalError.WRONG_STATUS_CODE.value


def test_getting_count_posts():
    received_posts = response.json()
    assert len(received_posts) == 3, GlobalError.WRONG_NUMBER_OF_POSTS.value


def test_validate_data():
    res = Response(response.json(), POST_SCHEMA)
    res.validate()
