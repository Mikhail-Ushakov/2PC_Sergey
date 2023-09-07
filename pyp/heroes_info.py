import json
from bs4 import BeautifulSoup
import requests

url = 'https://superheroapi.com/ids.html'
proxy = {'http': 'http://proxy.server:3128'}
response = requests.get(url, proxies=proxy).text
objec = BeautifulSoup(response, 'html.parser')
heroes_info = {}

for row in objec.find_all('tr'):
    ids, name = row.find_all('td')[0].get_text(), row.find_all('td')[1].get_text()
    heroes_info[name] = ids

with open('hero_info.json', 'w') as f:
    data = json.dumps(heroes_info)
    f.write(data)