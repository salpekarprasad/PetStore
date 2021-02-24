import requests
from Tests.constants import PET_ENDPOINT
from Tests.resources import ApiResources


def create_pet(pet):
    url1 = PET_ENDPOINT
    return requests.post(url1, json=pet.get_data(), headers={"Content-Type": "application/json"}, )


def get_pet_by_status_available():
    url2 = PET_ENDPOINT + ApiResources.getPetByStatus
    return requests.get(url2, params={'status': 'available'})


def get_pet_by_status_sold():
    url3 = PET_ENDPOINT + ApiResources.getPetByStatus
    return requests.get(url3, params={'status': 'sold'})


def get_pet_by_status_pending():
    url4 = PET_ENDPOINT + ApiResources.getPetByStatus
    return requests.get(url4, params={'status': 'pending'})


def update_pet_name_and_status(pet):
    url5 = PET_ENDPOINT
    return requests.put(url5, json=pet.get_data(), headers={"Content-Type": "application/json"}, )


def add_image(pet):
    pid = str(pet.petId)
    url4 = PET_ENDPOINT + pid + ApiResources.getImageResource
    files = {'file': open('./Tests/TestData/seal-csm.png', 'rb')}
    return requests.post(url4, files=files)