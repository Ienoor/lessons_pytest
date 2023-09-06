# https://my-json-server.typicode.com/typicode/demo/posts
import requests

from config import SERVICE_URL
from tests.base.response import Response
from tests.schemas.Posts import POST_SCHEMA

response = requests.get(SERVICE_URL)


def test_getting_status_code():
    Response(response).assert_status_code(200)


def test_getting_count_posts():
    Response(response).assert_count_items(3)


def test_validate_data():
    Response(response).validate(POST_SCHEMA)
