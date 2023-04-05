python smart_contract_client.py \
	-b 'http://34.77.109.175:8020/api' \
	-k 'basic_create_asset' \
	-d '{"channel": "mychannel",
        "msp": "Org1MSP",
        "orguid": "Org1_appuser",
        "assetid": "asset12",
        "title": "Large medical dataset",
        "size": 5,
        "owner": "Org1MSP",
        "value": 15,
        "publisher": "TRUSTS",
        "creator": "TRUSTS_RESEARCH",
        "contactPoint": "Joe Trusts",
        "keyword": "Medical",
        "authorisation": "OAuth",
        "dataAccess": "URL:www.example.com/data",
        "creationDate": "07/02/22",
        "license": "MIT",
        "format": ".csv:none:csv",
        "accessInterface": "Web:Local",
        "description": "A sample asset on the trusts platform"}'
