import requests
import json
import webbrowser
from pprint import pprint
import credentials

r = requests.get('https://api.thecatapi.com/v1/favourites/', headers=credentials.headers)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format', r.text)
else:
    print(content)
    
print('Zaloguj się - podaj login i hasło')
userId = 'agh2m'
name = 'Arkadiusz'

print('Witaj', name)
print("Twoje ulubione koty to:", favouriteCats)

