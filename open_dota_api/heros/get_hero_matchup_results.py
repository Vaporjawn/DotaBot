from open_dota_api.heros.get_hero_id import get_hero_id, get_hero_name
from open_dota_api.open_dota_interface import get_data


def get_hero_match_up(hero_id):

    query_id = get_hero_id(hero_id)

    hero_data = get_data('heroes', query_id, 'matchups')

    results = 'Total Games:\tHero:\tWin Rate:\n'

    for hero in hero_data:
        games_played = hero['games_played']
        wins = hero['wins']
        win_percentage = (wins / games_played) * 100

        results = results + str(games_played) + '\t' + get_hero_name(hero['hero_id']) + '\t' + ('%.3f' % win_percentage) + '\n'

    return results
