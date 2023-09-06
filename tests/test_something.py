# https://my-json-server.typicode.com/typicode/demo/posts
import requests

from config import SERVICE_URL
from src.enums.errors import GlobalError

response = requests.get(SERVICE_URL)


def test_getting_status_code():
    assert response.status_code == 200, GlobalError.WRONG_STATUS_CODE.value


def test_getting_count_posts():
    received_posts = response.json()
    assert len(received_posts) == 4, GlobalError.WRONG_NUMBER_OF_POSTS.value
