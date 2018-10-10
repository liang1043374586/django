import json
from urllib import request

header = {'Content-Type': 'application/json-rpc'}
url = 'http://zywlzabbix.zhiyingwl.com/api_jsonrpc.php'
token = "3dfb0e8bbe4cc7ef559d50632c4e6bde"

def getHostId(token):
    data = {
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
        "auth": token,

    }
    value = json.dumps(data).encode('utf-8')
    req = request.Request(url, headers=header, data=value)

    try:
        result = request.urlopen(req)
    except Exception as e:
        print("Auth Failed, Please Check Your Name And Password:", e)
    else:
        response = result.read()
        page = response.decode('utf-8')
        pageList = json.loads(page).get('result')
        result.close()
    return pageList

# hostId="java"
# if getHostId(token)[0].get('host') == hostId:
#     HostId = getHostId(token)[0].get('hostid')
# else:
#     print("get hist HostId error")
print(getHostId(token)[0].get('hostid'))

