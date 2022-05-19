import requests
import json
import api_key


def location(local):
    global res
    api_key_for_yandex = api_key.get_api_key()
    address = local
    params = dict(apikey=api_key_for_yandex, geocode=address)
    try:
        url = 'https://geocode-maps.yandex.ru/1.x/?format=json'
        res = requests.get(url, params=params)
    except:
        return "ошибка при выполнении запроса в API Яндекса"
    finally:
        point = json.loads(res.text)
        points = point['response']
        x = points['GeoObjectCollection']
        y = x['featureMember']
        z = y[0]
        c = z['GeoObject']
        p = c['Point']
        coor = p['pos']
        coordinates = coor.split()
    return coordinates

