import requests

# https://httpbin.org/basic-auth/jamesbond/secretagent

r = requests.get('https://httpbin.org/basic-auth/jamesbond/secretagent', auth=('jamesbond','secretagent'), verify=False)

print(r.text)