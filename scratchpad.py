import requests

url = "https://192.168.1.160/afa/api/v1/riskcheck/calculate?riskprofile=RiskProfile_Demo.xml"

payload = "{\r\n  \"traffic\": [\r\n    {\r\n      \"destination\": [\r\n        \"10.176.50.100\"\r\n      ],\r\n      \"id\": 100,\r\n      \"service\": [\r\n        \"tcp/30001\"\r\n      ],\r\n      \"source\": [\r\n        \"10.50.64.100\"\r\n      ]\r\n    }\r\n  ]\r\n}"
headers = {
  'Content-Type': 'text/plain',
  'Cookie': 'PHPSESSID=eblul2m909b1akv3ii8kkmfe14'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)