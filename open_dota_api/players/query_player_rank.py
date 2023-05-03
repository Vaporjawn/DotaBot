from open_dota_api import open_dota_interface


def get_player_rank(player_id):
    player_data = open_dota_interface.get_data('players', player_id, '')

    solo_rank = str(player_data['solo_competitive_rank'])
    party_rank = str(player_data['competitive_rank'])
    estimate_mmr = str(player_data['mmr_estimate'])

    return "Solo Rank: " + solo_rank + "\nParty Rank: " + party_rank + "\nEstimated MMR: " + estimate_mmr
