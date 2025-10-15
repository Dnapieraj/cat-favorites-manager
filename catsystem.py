import requests
import json
import webbrowser
from pprint import pprint
import credentials

def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print('Niepoprawny format', response.text)
    else:
        return content


def get_favourite_cats(userId):
    params = {
        'sub_id': userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params=params, headers=credentials.headers)
    return get_json_content_from_response(r)

def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search', headers=credentials.headers)
    
    return get_json_content_from_response(r)

    
print('Zaloguj się - podaj login i hasło')
userId = 'agh2m'
name = 'Arkadiusz'

print('Witaj', name)
favouriteCats = get_favourite_cats(userId)
print("Twoje ulubione koty to:", favouriteCats)
randomCat = get_random_cat()
print('Wylosowano kota: ', randomCat[0]["url"])

