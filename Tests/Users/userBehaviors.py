import requests
from Tests.constants import USER_ENDPOINT
from Tests.resources import ApiResources


def create_user(users):
    url = USER_ENDPOINT + ApiResources.createUserWithArray
    payload = []
    for user in users:
        payload.append(user.get_data())
    r = requests.post(url, json=payload)
    return r


def get_user(user):
    url = USER_ENDPOINT + user.uname
    return requests.get(url, headers={"accept": "application/json"}, )


def user_login(user):
    url = USER_ENDPOINT + ApiResources.getLogin
    return requests.get(url, params={'username': user.uname, 'password': user.pwd},
                        headers={'accept': 'application/json'})


def user_logout():
    url = USER_ENDPOINT + ApiResources.getLogout
    return requests.get(url, headers={'accept': 'application/json'})


def delete_user(user):
    url = USER_ENDPOINT + user.uname
    return requests.delete(url, headers={'accept': 'application/json'})

