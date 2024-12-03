from pprint import pprint

import requests
from data import Token

base_url = 'https://testapi.kelasotomesyen.com'

token = Token.value

#get method
resp = requests.get(f"{base_url}/items", headers=token)
pprint(resp.json())


def test_get_items():
    resp = requests.get(f"{base_url}/items", headers=token)
    status_code = resp.status_code

    assert status_code == 200