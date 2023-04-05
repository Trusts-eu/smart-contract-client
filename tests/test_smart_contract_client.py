import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from smart_contract_client.smart_contract_client import \
    make_request_to_smart_contract_api
from tests.data_items import data_items


URL_BLOCKCHAIN = 'http://34.77.109.175:8020/api'
send_request_to_smart_contract_api = \
    make_request_to_smart_contract_api(URL_BLOCKCHAIN)


def test_requests():
    for kind, data in data_items.items():
        yield is_ok, kind, data


def is_ok(kind, data):
    r = send_request_to_smart_contract_api(kind, data)
    assert r.json()['status'] == 'OK'
