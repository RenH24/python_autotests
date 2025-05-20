import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0238d215dd6e090822c8050b519ef441'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Рекс",
    "photo_id": 10
}

body_change = {
    "pokemon_id": "319385",
    "name": "Малой",
    "photo_id": 7
}

body_pokeball = {
    "pokemon_id": "319385"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)