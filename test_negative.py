import pytest


def test_user_not_found(api_get):
    response = api_get("/users/9999")
    assert response.status_code == 404


def test_post_not_found(api_get):
    response = api_get("/posts/9999")
    assert response.status_code == 404


@pytest.mark.parametrize("invalid_id", [0, -1, 99999])
def test_invalid_user_ids(invalid_id, api_get):
    response = api_get(f"/users/{invalid_id}")
    assert response.status_code == 404


def test_empty_response_for_missing_user(api_get):
    response = api_get("/users/9999")
    assert response.json() == {}