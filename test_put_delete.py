import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_update_post():
    updated_data = {
        "id": 1,
        "title": "Обновлённый заголовок",
        "body": "Обновлённое содержимое",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=updated_data)

    assert response.status_code == 200
    assert response.json()["title"] == "Обновлённый заголовок"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.json() == {}


def test_patch_post():
    patch_data = {
        "title": "Только заголовок изменился"
    }

    response = requests.patch(f"{BASE_URL}/posts/1", json=patch_data)

    assert response.status_code == 200
    assert response.json()["title"] == "Только заголовок изменился"