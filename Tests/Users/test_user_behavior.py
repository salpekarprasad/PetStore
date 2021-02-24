import pytest
from Tests.Users.user import *
from Tests.Users.userBehaviors import *


@pytest.mark.User_scenario_1
def test_add_user():
    user_1 = User(1001, 'quintype', 'Quin', 'Type', 'Quin.Type@gmail.com', 'QuinType@123', '+91-7506185115', 0)
    user_2 = User(1001, 'salpekap', 'Prasad', 'Salpekar', 'salpekarprasade@gmail.com', 'Salpekap@123', '+91-8087176290',
                  1)
    post_Res_1 = create_user([user_1, user_2])
    assert post_Res_1.status_code == 200
    assert post_Res_1.elapsed.total_seconds() < 3000


@pytest.mark.User_scenario_2
def test_get_user():
    user_1 = User(1001, 'quintype', 'Quin', 'Type', 'Quin.Type@gmail.com', 'QuinType@123', '+91-7506185115', 0)
    c_user = create_user([user_1])
    assert c_user.status_code == 200
    get_res = get_user(user_1)
    assert get_res.status_code == 200


@pytest.mark.User_scenario_3
def test_user_login():
    user_1 = User(1001, 'quintype', 'Quin', 'Type', 'Quin.Type@gmail.com', 'QuinType@123', '+91-7506185115', 0)
    get_login = user_login(user_1)
    assert get_login.status_code == 200
    login_msg = get_login.json()['message']
    print(login_msg)
    print(get_login.headers)
    assert int(get_login.headers['X-Rate-Limit']) == 5000


@pytest.mark.User_scenario_4
def test_user_logout():
    user_1 = User(1001, 'quintype', 'Quin', 'Type', 'Quin.Type@gmail.com', 'QuinType@123', '+91-7506185115', 0)
    get_login = user_login(user_1)
    assert get_login.status_code == 200
    get_logout = user_logout()
    assert get_logout.status_code == 200


@pytest.mark.User_scenario_5
def test_delete_user():
    user_1 = User(1001, 'quintype', 'Quin', 'Type', 'Quin.Type@gmail.com', 'QuinType@123', '+91-7506185115', 0)
    get_delete = delete_user(user_1)
    assert get_delete.status_code == 200
