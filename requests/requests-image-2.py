# NASA Astronomy Picture of the Day
# https://api.nasa.gov/apod

import requests

apiKey = '' # generated from https://api.nasa.gov/
payload = {'api_key':apiKey} # prepare the api key for the API

# Get the APOD data
r = requests.get('https://api.nasa.gov/planetary/apod',params=payload, verify=False)

print(r.content)

#data = r.json() # convert to JSON so we can select just the URL data

#print(data['url'])

#r2 = requests.get(data['url'], verify=False) # Get the actual photo

#print(r2.content)

#with open('nasa_apod.jpg','wb') as f: # Create the image file with the content
#	f.write(r2.content)