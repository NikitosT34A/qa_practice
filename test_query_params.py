import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts_by_user():
    # Получить все посты конкретного пользователя
    params = {"userId": 1}
    response = requests.get(f"{BASE_URL}/posts", params=params)

    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0
    # Все посты должны принадлежать пользователю 1
    for post in posts:
        assert post["userId"] == 1


def test_get_comments_by_post():
    # Получить все комментарии к конкретному посту
    params = {"postId": 1}
    response = requests.get(f"{BASE_URL}/comments", params=params)

    assert response.status_code == 200
    comments = response.json()
    assert len(comments) > 0
    for comment in comments:
        assert comment["postId"] == 1


def test_check_actual_url_with_params():
    # Посмотреть как выглядит URL с параметрами
    params = {"userId": 1, "id": 5}
    response = requests.get(f"{BASE_URL}/posts", params=params)

    print(f"\nИтоговый URL: {response.url}")
    assert response.status_code == 200


def test_filter_todos_by_completed():
    # Получить только выполненные задачи
    params = {"completed": "true"}
    response = requests.get(f"{BASE_URL}/todos", params=params)

    assert response.status_code == 200
    todos = response.json()
    for todo in todos:
        assert todo["completed"] == True