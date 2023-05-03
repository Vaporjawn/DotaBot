from maps.hero_dictionary import hero_name_to_id


def get_hero_id(hero_name):
    hero_name = ' '.join(hero_name)

    try:
        hero_id = hero_name_to_id[hero_name]
        return hero_name + 's hero ID is : ' + str(hero_id)

    except KeyError as e:
        return "could not find her with name: " + hero_name
