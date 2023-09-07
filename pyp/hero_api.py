import json
import requests
import pprint
import os

pp = pprint.PrettyPrinter(indent=4)
API_KEY = '10218686935504422'

with open('hero_info.json', 'r') as f:
    hero_info = json.loads(f.read())

class SuperHeroAPI():
    def __init__(self, API=API_KEY, data=hero_info):
        self._token = API
        self._data = data
        self._url = f'https://www.superheroapi.com/api/{self._token}'
        self._proxy = {'http': 'http://proxy.server:3128'}

    def get_hero(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}')

    def _parse_name(self, name):
        return name.lower().title()

    def _get_id(self, name):
        id = hero_info[name]
        return id

    def _parse_api(self, url):
        response = requests.get(url, proxies=self._proxy)
        return response.json()

    def download_image(self, name):
        image_url = self._get_hero_image_url(name)
        response = requests.get(image_url, proxies=self._proxy)
        with open(f"{name} image.jpg", 'wb') as f:
            f.write(response.content)
        input()
        os.remove(f'{name} image.jpg')

    def _get_hero_image_url(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        response = self._parse_api(self._url + f'/{hero_id}/image')
        return response['url']

    def hero_battle(self, name_1, name_2):
        name_1 = self._parse_name(name_1)
        name_2 = self._parse_name(name_2)

        hero_id_1 = self._get_id(name_1)
        hero_id_2 = self._get_id(name_2)

        response_1 = self._parse_api(self._url + f'/{hero_id_1}/powerstats')
        response_2 = self._parse_api(self._url + f'/{hero_id_2}/powerstats')

        stats_1 =  int(response_1['strength']) +  int(response_1['speed']) +  int(response_1['intelligence']) + int(response_1['durability']) + int(response_1['power']) + int(response_1['combat'])
        stats_2 =  int(response_2['strength']) +  int(response_2['speed']) +  int(response_2['intelligence']) + int(response_2['durability']) + int(response_2['power']) + int(response_2['combat'])

        if stats_1 > stats_2:
            return f'{name_1} победил {stats_1}!'
        else:
            return f'{name_2} победил {stats_2- stats_1}!'
    

objec = SuperHeroAPI()
# pp.pprint(objec.get_hero('a-bomb'))
#objec.download_image('Batman')
print(objec.hero_battle('Batman', 'Superman'))