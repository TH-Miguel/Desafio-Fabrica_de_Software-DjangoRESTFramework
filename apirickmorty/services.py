import requests

def get_characters():

    url = 'https://rickandmortyapi.com/api/character'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json
    else:
        response.raise_for_status()