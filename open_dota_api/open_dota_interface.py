import json
import requests

OPEN_DOTA_URL = 'https://api.opendota.com/api/'


def get_data(api_access_path, player_id):
    url = OPEN_DOTA_URL + api_access_path + '/' + player_id

    game_data = requests.get(url)

    if not (game_data.status_code == 200):
        print(f"Response code {game_data.status_code}. The request for ID {player_id} failed.")
        return None

    data = json.loads(game_data.text)

    return data
