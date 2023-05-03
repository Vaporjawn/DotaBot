from maps.hero_dictionary import hero_name_to_id


def get_hero_id(hero_name):

    try:
        hero_id = hero_name_to_id[hero_name]
        return str(hero_id)

    except KeyError as e:
        return "Could not find hero with name: " + hero_name


def get_hero_name(hero_id):

    for name, id in hero_name_to_id.items():
        if hero_id == id:
            return name
