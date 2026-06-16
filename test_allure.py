import allure
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@allure.title("Получение списка пользователей")
@allure.description("Проверяем что API возвращает 10 пользователей со статусом 200")
def test_get_users():
    with allure.step("Отправляем GET запрос на /users"):
        response = requests.get(f"{BASE_URL}/users")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем количество пользователей"):
        assert len(response.json()) == 10


@allure.title("Создание нового поста")
@allure.description("Проверяем что POST запрос создаёт пост и возвращает 201")
def test_create_post():
    with allure.step("Подготавливаем данные"):
        new_post = {"title": "Test", "body": "Body", "userId": 1}

    with allure.step("Отправляем POST запрос"):
        response = requests.post(f"{BASE_URL}/posts", json=new_post)

    with allure.step("Проверяем что пост создан"):
        assert response.status_code == 201