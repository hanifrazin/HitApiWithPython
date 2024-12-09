import json
import random

import pytest
import requests
from pprint import pprint

from faker import Faker
from faker_food import FoodProvider

from data.schema import *
from jsonschema import validate, ValidationError

base_url = 'https://testapi.kelasotomesyen.com'
id = 0
foodName = "test"
description = "test"
jumlah = 0


#get method
# resp = requests.get(f"{base_url}/items/1", headers=token)
# print(resp.status_code)
# print(resp.text)
# json_response = json.loads(resp.text)
# pprint(json_response)

# schema get item

def is_response_valid(resp):
    if not resp.text.strip():
        print("Respons kosong.")
        return False
    if resp.headers.get("Content-Type") != "application/json":
        print("Respons bukan JSON.")
        return False
    return True


def get_token():
    body = {
        "username": "admin",
        "password": "uHuY12#$"
    }
    resp = requests.post(f'{base_url}/login', json=body)

    if not is_response_valid(resp):
        return

    json_resp = json.loads(resp.text)
    return {"Authorization": f"Bearer {json_resp.get('token')}"}


def test_list_items():
    resp = requests.get(f'{base_url}/items', headers=get_token())
    global id, foodName, description, jumlah

    if not is_response_valid(resp):
        return

    json_resp = json.loads(resp.text)
    assert resp.status_code == 200
    assert len(json_resp) > 0
    assert type(json_resp) == list

    rand_index = random.randint(0, len(json_resp) - 1)
    id = json_resp[rand_index]["id"]
    foodName = json_resp[rand_index]["name"]
    description = json_resp[rand_index]["description"]
    jumlah = json_resp[rand_index]["quantity"]

    try:
        validate(resp.json(), schema=Schema.schema_list_item)
    except ValidationError as e:
        assert False, f'JSON Schema validation error: {e}'


def test_get_specific_items():
    global id, foodName
    resp = requests.get(f"{base_url}/items/{id}", headers=get_token())

    if not is_response_valid(resp):
        return

    status_code = resp.status_code
    json_response = json.loads(resp.text)
    iD = json_response.get('id')
    name = json_response.get('name')
    print(status_code)
    assert status_code == 200
    assert iD == id
    assert name == foodName

    try:
        validate(resp.json(), schema=Schema.schema_get_specific_item)
    except ValidationError as e:
        assert False, f'JSON Schema error: {e}'


def test_post_items():
    fake = Faker()
    fake.add_provider(FoodProvider)
    food = fake.dish()
    qty = fake.random_int(10,100)

    body = {
        "name": food,
        "description": "Jajanan Traditional",
        "quantity": qty
    }
    resp = requests.post(f"{base_url}/items", json=body, headers=get_token())

    if not is_response_valid(resp):
        return

    status_code = resp.status_code
    assert status_code == 201


def test_put_items():
    fake = Faker()
    fake.add_provider(FoodProvider)
    food = fake.dish()
    qty = fake.random_int(10, 100)

    body = {
        "name": food,
        "description": "Jajanan Pasar Shubuh",
        "quantity": qty
    }

    resp = requests.put(f"{base_url}/items/{id}", json=body, headers=get_token())

    if not is_response_valid(resp):
        return

    assert resp.status_code == 200


def test_delete_items():
    resp = requests.delete(f"{base_url}/items/{id}", headers=get_token())

    if not is_response_valid(resp):
        return

    json_resp = json.loads(resp.text)
    assert resp.status_code == 200
    assert json_resp.get('message') == "Item deleted"

