# Find something to do using http://www.boredapi.com/

import requests

r = requests.get('https://www.boredapi.com/api/activity/', verify=False)

print(r.content)