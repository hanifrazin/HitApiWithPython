import json
import requests
from pprint import pprint
from data import Schema
from jsonschema import validate, ValidationError

base_url = 'https://testapi.kelasotomesyen.com'

#get method
# resp = requests.get(f"{base_url}/items/1", headers=token)
# print(resp.status_code)
# print(resp.text)
# json_response = json.loads(resp.text)
# pprint(json_response)

# schema get item

def get_token():
    body = {
        "username": "admin",
        "password": "uHuY12#$"
    }
    resp = requests.post(f'{base_url}/login', json=body)
    json_resp = json.loads(resp.text)
    return {"Authorization": f"Bearer {json_resp.get('token')}"}

def test_get_items():
    resp = requests.get(f"{base_url}/items/1", headers=get_token())

    status_code = resp.status_code
    json_response = json.loads(resp.text)
    id = json_response.get('id')
    name = json_response.get('name')

    assert status_code == 200
    assert id == 1
    assert name == 'Dodol'

    try:
        validate(resp.json(), schema=Schema.schema_get_item)
    except ValidationError as e:
        assert False, f'JSON Schema error: {e}'

def test_post_items():
    body = {
        "name": "Bakso Tahu",
        "description": "Jajanan Traditional",
        "quantity": 10
    }
    resp = requests.post(f"{base_url}/items", json=body, headers=get_token())

    status_code = resp.status_code
    json_response = json.loads(resp.text)
    pprint(json_response)


test_post_items()

