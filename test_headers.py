import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_response_has_json_content_type():
    response = requests.get(f"{BASE_URL}/users")
    content_type = response.headers["Content-Type"]
    assert "application/json" in content_type


def test_request_with_custom_headers():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Custom-Header": "qa-test"
    }
    response = requests.get(f"{BASE_URL}/users", headers=headers)
    assert response.status_code == 200


def test_check_all_response_headers():
    response = requests.get(f"{BASE_URL}/users")
    print("\nВсе заголовки ответа:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    assert "Content-Type" in response.headers


def test_login_and_get_token():
    # Имитируем авторизацию — создаём пользователя и получаем id как "токен"
    credentials = {
        "username": "qa_user",
        "password": "secret"
    }
    response = requests.post(
        f"{BASE_URL}/users",
        json=credentials
    )
    assert response.status_code == 201
    user_id = response.json()["id"]
    assert user_id is not None
    print(f"\nСоздан пользователь с id: {user_id}")


def test_request_with_auth_header():
    # В реальных проектах токен получают через login endpoint
    # Здесь симулируем передачу токена в заголовке
    fake_token = "test-token-12345"
    headers = {
        "Authorization": f"Bearer {fake_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}/users", headers=headers)

    # jsonplaceholder игнорирует заголовки и возвращает 200
    # На реальном API без токена было бы 401
    assert response.status_code == 200
    print(f"\nЗаголовок Authorization принят, статус: {response.status_code}")