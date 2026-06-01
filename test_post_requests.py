import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post():
    new_post = {
        "title": "Мой первый пост",
        "body": "Содержимое поста",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    assert response.status_code == 201
    assert response.json()["title"] == "Мой первый пост"
    assert response.json()["userId"] == 1


def test_create_user():
    new_user = {
        "name": "Nikita",
        "username": "nikita_qa",
        "email": "nikita@test.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=new_user)

    assert response.status_code == 201
    assert response.json()["name"] == "Nikita"
    assert response.json()["email"] == "nikita@test.com"