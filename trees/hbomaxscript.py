import requests
url = 'https://play.hbomax.com/player/urn:hbo:episode:GXyL-_A6im8J6pQEAAAGD'

resp = requests.get(url)
print(resp)
