# Write API modules : done
#  

#!/usr/bin/python


import requests 
import json

### Parameters ####
username = 'admin'
password = 'algosec'
base_url = 'https://192.168.1.160'
device = 'Flower_ASA'


def afa_login(base_url,api_login,api_password):
    print("Getting token...")
    s = requests.Session() 
    data_get = {'username': api_login,
                'password': api_password,
                'domain': ''}
    r = s.post(base_url + '/fa/server/connection/login', data=data_get, verify=False)
    if r.ok:
        auth_token = r.cookies['PHPSESSID']
        cookies = dict(r.cookies)
        print("Token: " + auth_token)
        return auth_token, cookies
    
    else:
        print("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))


def afa_risky_rules(base_url, token, entity, entity_type):

    params = {'session': token,
            'entity': entity,
            'entityType': entity_type}

    r = requests.get(base_url + '/fa/server/risks/riskyRules', params=params, verify=False)
    return json.loads(r.text)



def afa_risk_check(base_url, cookies, source, destination, service):

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    params = {'riskprofile': 'RiskProfile_Demo.xml'}
    payload = "{\r\n  \"traffic\": [\r\n    {\r\n      \"destination\": [\r\n        \"10.176.50.100\"\r\n      ],\r\n      \"id\": 100,\r\n      \"service\": [\r\n        \"tcp/30001\"\r\n      ],\r\n      \"source\": [\r\n        \"10.50.64.100\"\r\n      ]\r\n    }\r\n  ]\r\n}"
    # TODO: refactor request to use object below.
    payload2 = { "traffic" : [
            {
                "destination": ["10.176.50.100"],
                "id": 100,
                "service": ["tcp/30001"],
                "source": ["10.50.64.100"]
            }
        ]
    }
    r = requests.post(  base_url + '/afa/api/v1/riskcheck/calculate', 
                        data=payload,
                        params=params, 
                        verify=False, 
                        cookies=cookies,
                        headers=headers
    )
    # print(r.request.headers)
    # print(r.request.body)
    # print(r.status_code)
    # print(r.json)
    # print(r.raw)
    # print(r.text)
    # print(r.request.prepare_cookies)
    # print(r.headers)
    # print(r)
    return json.loads(r.text)


if __name__ == "__main__":
    
    source = '10.10.10.10'
    destination = '8.8.8.8'
    service = 'tcp/23'
    token, cookies = afa_login(base_url=base_url, api_login=username, api_password=password)
    risks = afa_risk_check(base_url=base_url, cookies=cookies, source=source, destination=destination, service=service)
    print(json.dumps(risks, indent=4, sort_keys=True))







