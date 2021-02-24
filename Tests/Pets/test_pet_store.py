from Tests.Pets.petStore import *
from pet import Pet
import pytest


@pytest.mark.Pet_scenario_1
def test_add_pet_by_status_available():
    pet_1 = Pet(101, 102, 'cat', 'available')
    post_Res = create_pet(pet_1)
    assert post_Res.status_code == 200
    assert post_Res.elapsed.total_seconds() < 3000
    return post_Res.json()


@pytest.mark.Pet_scenario_1
def test_add_pet_by_status_sold():
    pet_2 = Pet(201, 202, 'dog', 'sold')
    post_Res = create_pet(pet_2)
    assert post_Res.status_code == 200
    assert post_Res.elapsed.total_seconds() < 3000
    return post_Res.json()


@pytest.mark.Pet_scenario_1
def test_add_pet_by_status_pending():
    pet_1 = Pet(101, 102, 'rat', 'pending')
    post_Res = create_pet(pet_1)
    assert post_Res.status_code == 200
    assert post_Res.elapsed.total_seconds() < 3000
    return post_Res.json()


def test_get_pet_by_status_available():
    res = test_add_pet_by_status_available()
    get_res = get_pet_by_status_available()
    assert get_res.status_code == 200
    for i in get_res.json():
        if i['id'] == res['id']:
            assert i['id'] == res['id']


@pytest.mark.Pet_scenario_2
def test_get_pet_by_status_sold():
    res = test_add_pet_by_status_sold()
    get_res = get_pet_by_status_sold()
    assert get_res.status_code == 200
    for i in get_res.json():
        if i['id'] == res['id']:
            assert i['id'] == res['id']


def test_get_pet_by_status_pending():
    res = test_add_pet_by_status_pending()
    get_res = get_pet_by_status_pending()
    assert get_res.status_code == 200
    for i in get_res.json():
        if i['id'] == res['id']:
            assert i['id'] == res['id']


@pytest.mark.Pet_scenario_3
def test_updatePet():
    pet = Pet(201, 202, 'sparrow', 'available')
    put_Res = update_pet_name_and_status(pet)
    print(put_Res.status_code)
    print(put_Res.json())
    assert put_Res.json()['name'] == 'sparrow'
    assert put_Res.json()['status'] == 'available'


@pytest.mark.Pet_scenario_4
def test_addImage():
    pet = Pet(101, 102, 'cat', 'available')
    img_Res = add_image(pet)
    assert img_Res.status_code == 200
