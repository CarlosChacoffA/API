# Docs
# https://www.zabbix.com/documentation/3.2/manual/api
# http://docs.python-requests.org/en/master/api/#request-sessions
# http://docs.python-requests.org/en/master/api/#requests.Response
# https://realpython.com/api-integration-in-python/
# https://zabbix.org/wiki/Docs/api/libraries

import requests
import json

server = "http://opzabbix.neogistica.com/zabbix"
username = "neoapi"
password = "n3o5tgzbx"

headers = {'Content-type': 'application/json'}
# api_data = json.dumps({"jsonrpc": "2.0", "method": "user.login", "params": {"user": username, "password": password}, "id": 1})
# api_data = json.dumps({'jsonrpc': '2.0', 'method': 'apiinfo.version', 'id': 1, 'params': {}})
api_data = json.dumps({
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "id": 2,
    "auth": "50638417a9dd3e8fc1d75e8dcd4b3227"
	})
api_url = server + "/api_jsonrpc.php"
response = requests.post(api_url, data=api_data, proxies={}, headers=headers)
#print("Text: ", response.text)
print("Json: ", response.json())
#print("Json result: ", response.json()['result'])