import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_status_code():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200


def test_get_users_count():
    response = requests.get(f"{BASE_URL}/users")
    users = response.json()
    assert len(users) == 10


def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/users/1")
    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"


def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/999")
    assert response.status_code == 404