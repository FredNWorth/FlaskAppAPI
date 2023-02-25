import requests

''' Methods
    PUT: headers (name,age)
    DELETE: params <id>
    GET: params (optional) id '''

url = "http://192.168.0.28:5000"
params = {'name': 'Brock Shears', 'age': "1"}
headers = {}
result = requests.get(url=url, params=params, headers=headers)
result.raise_for_status()
print(result.text)
