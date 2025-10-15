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

def add_favourite_cat(catId, userId):
    catData = {
        'image_id': catId,
        'sub_id': userId
    }
    r = requests.post('https://api.thecatapi.com/v1/favourites/', json=catData, headers=credentials.headers)
    
    return get_json_content_from_response(r)

def remove_favourite_cat(userId, favouriteCatId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/' + favouriteCatId, headers=credentials.headers)
    
    return get_json_content_from_response(r)

    
print('Zaloguj się - podaj login i hasło')
userId = 'agh2m'
name = 'Daniel'

print('Witaj', name)
favouriteCats = get_favourite_cats(userId)
print("Twoje ulubione koty to:", favouriteCats)
randomCat = get_random_cat()
print('Wylosowano kota: ', randomCat[0]["url"])

addToFavourites = input('Czy chcesz dodać kota do ulubionych? T/N')

if addToFavourites.upper() == 'T':
    print(add_favourite_cat(randomCat[0]["id"], userId))
else:
    print('Kot nie został dodany do ulubionych')
    
favouriteCatsById = {
    favouriteCat['id'] : favouriteCat['image']['url']
    for favouriteCat in favouriteCats
}
print(favouriteCatsById)

favouriteCatId = input('Czy chcesz usunąć kota z ulubionych? Podaj jego ID: ')

print(remove_favourite_cat(userId, favouriteCatId))