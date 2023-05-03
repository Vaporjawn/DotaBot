from open_dota_api.heros.get_hero_matchup_results import get_hero_match_up
from open_dota_api.players import query_player_rank
from open_dota_api.heros.get_hero_id import get_hero_id


def handle_responses(message) -> str:
    p_message = message.lower()

    p_message_list = p_message.split()
    command = p_message_list[0]

    if command == '!help':
        return '!getrank {Steam ID}: Returns the rank of the entered user\n' \
               '!getheroid {English name of hero}: returns the ID number of the entered hero\n' \
               '!getheromatchup {English name of hero}: returns the entered heroes match ups against other heroes in ' \
               'order of most games played against\n'

    if len(p_message_list) != 1:
        dota_id = p_message_list[1:]
        dota_id = ' '.join(dota_id)

        if command == '!getrank':
            return query_player_rank.get_player_rank(dota_id)
        elif command == '!getheroid':
            return get_hero_id(dota_id)
        elif command == '!getheromatchup':
            return get_hero_match_up(dota_id)
