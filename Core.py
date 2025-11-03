from Pokemon import Pokemon
from Location import Location
from Sphere import Sphere



def construct_full_pokemon_set(pokedex_data) -> dict:
    """
    Creates a dict of all Pokémon from an input pokedex YAML.

    args:
        pokedex_data (list of dicts, one for each mon)

    returns:
        all_pokemon (dict of Pokemon objects where keys are names of Pokémon)
    """
    # create empty dict
    all_pokemon = dict()

    # iterate through each dict in the list pokedex_data
    for cur_mon in pokedex_data:
        # create object of class Pokemon for current mon
        cur_mon_obj = Pokemon(
            name=cur_mon["name"],
            species_line=cur_mon["species_line"],
            evo_stage=cur_mon["evo_stage"],
            is_fully_evolved=cur_mon["is_fully_evolved"],
            is_legendary=cur_mon["is_legendary"],
            types=cur_mon["types"],
            base_stat_total=cur_mon["base_stat_total"],
            hm_learnset=cur_mon["hm_learnset"],
            evolution_method_required=cur_mon["evolution_method_required"]
            )
        
        # add current mon's Pokemon object to dict
        all_pokemon[cur_mon["name"]] = cur_mon_obj

    return all_pokemon

def construct_full_location_set(location_data) -> dict:
    """
        Creates a dict of all Locations from an input locations YAML.

        args:
            location_data (list of dicts, one for each location)

        returns:
            all_locations (dict of Location objects where keys are names of locations)
        """
    # create empty dict
    all_locations = dict()

    # iterate through each dict in the list location_data
    for cur_loc in location_data:
        # create object of class Location for current location
        cur_loc_obj = Location(
            name=cur_loc["map_name"],
            walk=cur_loc["walk"] if "walk" in cur_loc else None,
            surf=cur_loc["surf"] if "surf" in cur_loc else None,
            old_rod=cur_loc["old_rod"] if "old_rod" in cur_loc else None,
            good_rod=cur_loc["good_rod"] if "good_rod" in cur_loc else None,
            super_rod=cur_loc["super_rod"] if "super_rod" in cur_loc else None,
            poke_flute=cur_loc["poke_flute"] if "poke_flute" in cur_loc else None,
            static_encounter=cur_loc["static_encounter"] if "static_encounter" in cur_loc else None,
            trade=cur_loc["trade"] if "trade" in cur_loc else None,
            gift=cur_loc["gift"] if "gift" in cur_loc else None,
            fossil_restore=cur_loc["fossil_restore"] if "fossil_restore" in cur_loc else None,
            prize_window=cur_loc["prize_window"] if "prize_window" in cur_loc else None
        )

        # add current loc's Location object to dict
        all_locations[cur_loc["map_name"]] = cur_loc_obj

    return all_locations

def construct_spheres(progression_data, all_locations) -> dict:
    """
        Creates a set of all Spheres from an input progression YAML.

        args:
            progression_data (from progression YAML)

        returns:
            all_spheres (dict of Sphere objects, where keys are numbers (int) of spheres)
    """
    # create empty set
    all_spheres = dict()

    # iterate through each sphere in the progression data 'spheres' list
    for cur_sphere in progression_data['world']['spheres']:
        # get the sphere number and contents (list of maps and items)
        sphere_num = cur_sphere['sphereNum']
        sphere_contents = cur_sphere['contents']
        maps, items = [], []

        # add all the maps and items to lists for each type
        for element in sphere_contents:
            if element['type'] == 'map':
                map_object = all_locations[element['name']]
                maps.append(map_object)
            elif element['type'] == 'item':
                items.append(element['name'])
            #TODO add a fallback here to check for any other type and raise an Error?

        # create a Sphere object and add it to the dict of all spheres, where the key is the sphere num (1, 2, 3, etc.)
        all_spheres[sphere_num] = Sphere(maps, items)

    return all_spheres

def build_pools():
    """
        Takes all_spheres as input and expands all Spheres into pools/inventories.
    """
    return

def get_parent_mon():
    # how would this work for branching evos like Eevee?
    return

def get_immediate_child_mon(pokemon, all_pokemon) -> Pokemon | None:
    stage = pokemon.evo_stage
    # check if this is already a basic Pokemon, and return None if so
    if stage == 1:
        return None
    species = pokemon.species_line
    immediate_child = None
    for mon in all_pokemon.keys():
        if all_pokemon[mon].species_line == species and all_pokemon[mon].evo_stage == (stage - 1):
            immediate_child = all_pokemon[mon]
            break

    return immediate_child

def test_whether_locations_are_all_valid_in_progression_file(all_locations):
    """
        unfinished
    """
    # source of truth for assert statement below
    location_names = {loc.name for loc in all_locations}
    # for item in sphereContents:
    #     print(item['name'])
    #     assert item['name'] in location_names

    return