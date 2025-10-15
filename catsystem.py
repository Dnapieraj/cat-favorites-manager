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
    result = get_json_content_from_response(r)
    if result and len(result) > 0:
        return result[0]
    return None

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
if favouriteCats:
    print("Twoje ulubione koty to:", favouriteCats)
else:
    print("Brak ulubionych kotów")

randomCat = get_random_cat()
if randomCat:
    print('Wylosowano kota: ', randomCat["url"])
    
    addToFavourites = input('Czy chcesz dodać kota do ulubionych? T/N: ')
    newlyAddedCatInfo = {}

    if addToFavourites.upper() == 'T':
        resultFromAddingFavouriteCat = add_favourite_cat(randomCat["id"], userId)
        if resultFromAddingFavouriteCat:
            newlyAddedCatInfo = {resultFromAddingFavouriteCat['id'] : randomCat["url"]}
    else:
        print('Kot nie został dodany do ulubionych')
        
    if favouriteCats:
        favouriteCatsById = {
            favouriteCat['id'] : favouriteCat['image']['url']
            for favouriteCat in favouriteCats
        }
        favouriteCatsById.update(newlyAddedCatInfo)
        print(favouriteCatsById)

        favouriteCatId = input('Czy chcesz usunąć kota z ulubionych? Podaj jego ID (Enter = pomiń): ')
        if favouriteCatId:
            print(remove_favourite_cat(userId, favouriteCatId))
    else:
        print("Brak kotów do usunięcia")
else:
    print("Nie udało się pobrać kota")