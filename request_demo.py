
import requests

url = "https://api.quotable.io/random"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['content'])
else:
    print("Error:", response.status_code)

print("=="*40)

import urllib.request
import json

url = "https://api.quotable.io/random"
response = urllib.request.urlopen(url)

if response.status == 200:
    data = json.loads(response.read().decode())
    print(data['content'])
else:
    print("Error:", response.status)

print("=="*40)

import http.client
import json

conn = http.client.HTTPSConnection("api.quotable.io")
conn.request("GET", "/random")

response = conn.getresponse()
if response.status == 200:
    data = json.loads(response.read().decode())
    print(data['content'])
else:
    print("Error:", response.status)
