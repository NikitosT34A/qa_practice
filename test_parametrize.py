import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_user_exists(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch"),
])
def test_user_name(user_id, expected_name):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.json()["name"] == expected_name