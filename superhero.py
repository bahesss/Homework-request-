import requests
import json

url = 'https://akabab.github.io/superhero-api/api'

if __name__ == '__main__':
    request = requests.get(url + '/all.json')

    name_stat = dict()

    obj = json.loads(request.text)

    for hero in obj:
        if hero['name'] in ('Hulk', 'Captain America', 'Thanos'):
            name_stat[hero['name']] = hero['powerstats']['intelligence']

    print(max(name_stat, key=name_stat.get))
