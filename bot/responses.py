from open_dota_api import query_player_rank


def handle_responses(message) -> str:
    p_message = message.lower()

    p_message_list = p_message.split()
    command = p_message_list[0]

    if command[0] != '!':
        if command == '!help':
            return 'I currently have no functionality \n' \
                    'In the future, try these commands!:\n' \
                    '\t!getrank {Steam ID} - return the rank of the user\n' \
                    '\t!getwinrate {Steam ID} - return the winrate of the user\n' \
                    '\t!last5 {Steam ID} - return the outcome of the users last 5 games\n' \
                    '\t!getstanding - return the current rank of the "Wood League Guild\n'

        if len(p_message_list) != 1:
            dota_id = p_message_list[1]

            if command == '!getstanding':
                return 'This is where I would display the guild standing... IF I COULD!'
            elif command == '!getrank':
                return query_player_rank.get_player_rank(dota_id)
