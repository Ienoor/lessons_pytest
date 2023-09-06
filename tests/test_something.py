# https://my-json-server.typicode.com/typicode/demo/posts
import requests

from config import SERVICE_URL
from src.enums.errors import GlobalError


def test_getting_posts():
    response = requests.get(SERVICE_URL)
    assert response.status_code == 200, GlobalError.WRONG_STATUS_CODE.value
