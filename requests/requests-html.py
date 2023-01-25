# Get webpage source using the Python Requests library
import requests

website = 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'

r = requests.get(website, verify=False)
print(r.text)

'''
Other response properties:

r.content     - Returns the content of the response, in bytes
r.headers     - Returns a dictionary of response headers
r.json()      - Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
r.ok 	      - Returns True if status_code is less than 400, otherwise False
r.reason      - Returns a text corresponding to the status code
r.request     - Returns the request object that requested this response
r.status_code - Returns a number that indicates the status (200 is OK, 404 is Not Found)
r.text 	      - Returns the content of the response, in unicode
r.url 	      - Returns the URL of the response

'''