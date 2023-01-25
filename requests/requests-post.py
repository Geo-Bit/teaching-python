# Using POST request with python requests library

import requests

payload = {
    'username':'James',
    'password':'Sp3cial@g3n7'
}

r = requests.post('https://httpbin.org/post', data=payload, verify=False)
print(r.text)

r_json = r.json()
print(r_json)
print(r_json['form']['password']) # Print only the password