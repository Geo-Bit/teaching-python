# Get an Image using Python requests library
# https://xkcd.com/353/

import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png', verify=False) # URL of comic image

print(r.content) # returns the image bytes

with open('python_comic.png', 'wb') as f:
    f.write(r.content)