def test_status_code(users_response):
    assert users_response.status_code == 200

def test_users_count(users_response):
    assert len(users_response.json()) == 10

def test_single_user_id(single_user_response):
    user = single_user_response.json()
    assert user["id"] == 1

def test_single_user_name(single_user_response):
    user = single_user_response.json()
    assert user["name"] == "Leanne Graham"