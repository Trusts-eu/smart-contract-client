import argparse
import json
import os
import requests

from url_mapping import URL_SUBDIRECTORIES


def make_request_to_smart_contract_api(base_url):

    headers = {'Content-Type': 'application/json'}

    def __create_urls(base_url):
        return {method_name: os.path.join(base_url, url_subdirectory)
                for method_name, url_subdirectory
                in URL_SUBDIRECTORIES.items()}

    urls = __create_urls(base_url)

    def send_request_to_smart_contract_api(kind, data):
        return requests.get(urls[kind],
                            headers=headers,
                            data=json.dumps(data))

    return send_request_to_smart_contract_api


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Send a request to the smart contracts API.")
    parser.add_argument('-b', '--blockchain_url')
    parser.add_argument('-k', '--kind')
    parser.add_argument('-d', '--data', type=json.loads)

    args = parser.parse_args()

    send_request_to_smart_contract_api = \
        make_request_to_smart_contract_api(args.blockchain_url)
    r = send_request_to_smart_contract_api(args.kind,
                                           args.data)
    print(r.json())
