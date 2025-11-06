from Pokemon import Pokemon
from Location import Location
from Sphere import Sphere


def construct_full_pokemon_set(pokedex_data) -> dict[str, Pokemon]:
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

def construct_full_location_set(location_data) -> dict[str, Location]:
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

def construct_spheres(progression_data, all_locations) -> dict[int, Sphere]:
    """
        Creates a set of all Spheres from an input progression YAML.

        args:
            progression_data (from progression YAML), all_locations (dict of all Location objects)

        returns:
            all_spheres (dict of Sphere objects, where keys are numbers (int) of spheres)
    """
    # create empty set
    all_spheres = dict()

    # iterate through each sphere in the progression data 'spheres' list
    for cur_sphere in progression_data['world']['spheres']:
        # get the sphere number and contents (list of maps items, acquisition_unlocks)
        sphere_num = cur_sphere['sphereNum']
        sphere_contents = cur_sphere['contents']
        maps, items, acquisition_unlocks = [], [], []

        # add all the maps and items to lists for each type
        for element in sphere_contents:
            if element['type'] == 'map':
                map_object = all_locations[element['name']]
                maps.append(map_object)
            elif element['type'] == 'item':
                items.append(element['name'])
            elif element['type'] == 'acquisition_unlock':
                acquisition_unlocks.append(element['name'])
            #TODO add a fallback here to check for any other type and raise an Error?

        # create a Sphere object and add it to the dict of all spheres, where the key is the sphere num (1, 2, 3, etc.)
        all_spheres[sphere_num] = Sphere(maps, items, acquisition_unlocks)

    return all_spheres


def build_pools(all_spheres, all_pokemon, starting_acquisition_methods):
    """
        Takes all_spheres as input and expands all Spheres into pools (available Pokemon in a Sphere).
    """
    all_pools = dict()

    # to keep track of current enabled acquisition methods that unlock Location sublists (old_rod, surf, etc.)
    enabled_acquisition_methods = [method for method in starting_acquisition_methods]

    # to keep track of current set of items that enable evolution (stones, etc.)
    inventory = []

    spheres_checked = {}

    # iterate over all spheres from all_spheres dict
    for sphere_num in all_spheres.keys():
        locations = all_spheres[sphere_num].maps
        items = all_spheres[sphere_num].items
        acquisition_unlocks = all_spheres[sphere_num].acquisition_unlocks
        for item in items:
            if item not in inventory:
                inventory.append(item)
        for unlock in acquisition_unlocks:
            if unlock not in enabled_acquisition_methods:
                enabled_acquisition_methods.append(unlock)

        # build list of Pokemon by iterating over each location in locations and adding all its Pokemon (the object version, from all_pokemon) to a list
        for location_obj in locations:
            for method in enabled_acquisition_methods:
                # get list stored in that attribute (like location.walk)
                method_list = getattr(location_obj, method, None)
                if method_list:
                    print(f"\n{method.upper()} encounters at {location_obj.name}:")
                    for pokemon in method_list:
                        print(f"  - {pokemon}")
        # here, will need code that now ALSO goes back and iterates over all the locations in PREV spheres (using the ones kept track of in spheres_checked)
        # and then compare enabled_acquisition_methods at THIS point to the point in time when the previous spheres were iterated over. so if their "methods_expanded"
        # list doesnt match the current enabled_acquisition_methods list, the new ones from the PREV spheres locations need to be expanded and added to CURRENT pool.
        # then, their "methods_expanded" list in spheres_checked dict needs to be updated so it matches the current one (so we don't do it again next iteration).
        spheres_checked[sphere_num] = {"methods_expanded": [method for method in enabled_acquisition_methods]}


    # each map in each sphere is a Location object
    # will also need the list of all_pokemon as input for this function
    # i will probably first need to make sure all the lists of pokemon in each Location object can be mapped to the actual Pokemon objects
    # I think the pools should be made up of Pokemon objects, not simply strings of pokemon names. This way, their attributes can be checked when we need to filter them out of the generation
    # due to config constraints, etc. (like "don't generate pokemon of X type")
    # final all_pools should be a dict of pool_num (int) as keys and another dict ({"pool": [list, of, pokemon objects], "inventory": [list, of items]}) as the values
    # but maybe the "inventory" part is actually not necessary if we're only using a Sphere's inventory to build the pools. Yeah, probably this. So pool just needs to be a list of pokemon objects
    return

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