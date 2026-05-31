import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def users_response():
    return requests.get(f"{BASE_URL}/users")


@pytest.fixture
def single_user_response():
    return requests.get(f"{BASE_URL}/users/1")