from Pokemon import Pokemon
from Location import Location
from Sphere import Sphere
import random

def generate_final_party(all_pools, all_pokemon, config_data: dict, meta_data: dict, n: int = 6):
    """
    Generates a final party of Pokemon.
    """
    iterations = 0
    final_party = []

    # include a random starter if include_starter is selected in config
    if config_data["include_starter"]:
        rand_starter_species = random.choice(meta_data["starter_species"])
        matching_pokemon = [
            all_pokemon[mon] for mon in all_pokemon
            if all_pokemon[mon].species_line == rand_starter_species and all_pokemon[mon].is_fully_evolved #TODO change this to match highest allowed stage if NFE are allowed
        ]
        if matching_pokemon:
            chosen_starter = random.choice(matching_pokemon)
        else:
            chosen_starter = None
        final_party.append(chosen_starter)

    # iteratively build a party that is valid according to the config options
    while len(final_party) < n:
        rand_mon = generate_random_mon(all_pokemon)

        # check if the new Pokemon makes the party valid
        if is_party_valid(final_party + [rand_mon], bool(len(final_party + [rand_mon]) == n), config_data, meta_data): #TODO if the 6th pokemon cannot fulfill the requirement to have all HM coverage, this will be an endless loop
            final_party.append(rand_mon)
        iterations+=1
    print("iterations for final party generation:", iterations)
    #TODO add separate check here to see if party is valid for hm coverage, if not maybe we can recursively return this function and try the whole thing again
    # or simply have a timeout failsafe thing for all generations so we auto-retry
    # might need to pass a time variable around to all these functions
    return final_party

def is_party_valid(party, is_party_full, config_data, meta_data) -> bool:

    # set up meta data
    starter_species = meta_data["starter_species"]

    # set up config options
    include_starter = config_data["include_starter"]
    allow_not_fully_evolved = config_data["allow_not_fully_evolved"]
    allow_legendaries = config_data["allow_legendaries"]
    allow_duplicate_species = config_data["allow_duplicate_species"]
    allow_dual_type = config_data["allow_dual_type"]
    prescribed_type = config_data["prescribed_type"]
    type_distribution = config_data["type_distribution"]
    blacklist = config_data["blacklist"]
    included_evo_methods = [em for em in config_data["included_evo_methods"] if config_data["included_evo_methods"][em] == True]
    bst_max = config_data["bst_max"]
    bst_min = config_data["bst_min"]
    ensure_hm_coverage = set([hm for hm in config_data["ensure_hm_coverage"] if config_data["ensure_hm_coverage"][hm] == True])
    included_acquisition_methods = config_data["included_acquisition_methods"] #TODO this doesn't make sense here since we only have all_pokemon, needs to be checked in is_party_viable()

    # immediate False if these checks fail
    if not allow_duplicate_species:
        species_lines = [m.species_line for m in party]
        if len(species_lines) != len(set(species_lines)):
            return False

    if type_distribution != 'anything_goes':
        # this bool(...) expression evaluates to True if all Pokemon in party share at least one common type, False otherwise
        if (type_distribution == 'all_share_one_type') and not (bool(set.intersection(*(set(mon.types) for mon in party)))):
            return False
        # this expression evaluates to True if no Pokemon in party share any types, False otherwise
        if (type_distribution == 'no_overlap') and not (len({t for mon in party for t in mon.types}) == sum(len(mon.types) for mon in party)):
            return False

    if is_party_full:
        party_hm_coverage = set({hm for mon in party for hm in mon.hm_learnset})
        if not (ensure_hm_coverage.issubset(party_hm_coverage)):
            return False

    # checks against config options
    for mon in party:
        if mon.name in blacklist:
            return False
        if (include_starter == False) and (mon.species_line in starter_species): #TODO do we need this one?
            return False
        if (allow_not_fully_evolved == False) and (mon.is_fully_evolved == False):
            return False
        if (allow_legendaries == False) and (mon.is_legendary):
            return False
        if (allow_dual_type == False) and (len(mon.types) > 1):
            return False
        if (prescribed_type != 'none') and (prescribed_type not in mon.types):
            return False
        if mon.evolution_method_required not in included_evo_methods:
            return False
        if bst_max != 'none':
            if mon.base_stat_total > bst_max:
                return False
        if bst_min != 'none':
            if mon.base_stat_total < bst_min:
                return False


    return True

def is_party_progression_viable(all_pools) -> bool:
    # TODO I think pools will be needed as an argument so you can validate stone evo pokemon (check if stone is in inventory)
    # TODO plus all other checks against pools obviously lol
    return

def generate_random_mon(all_pokemon: dict[str, 'Pokemon']) -> 'Pokemon':
    """
    Generates a random Pokemon object.

    args:
        all_pokemon (dict of Pokemon objects)

    returns:
        random_pokemon
    """

    return random.choice(list(all_pokemon.values()))

def construct_full_pokemon_set(pokedex_data) -> dict[str, Pokemon]:
    """
    Creates a dict of all Pokemon from an input Pokedex YAML.

    args:
        pokedex_data (list of dicts, one for each mon)

    returns:
        all_pokemon (dict of Pokemon objects where keys are names of Pokemon)
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
            purchase=cur_loc["purchase"] if "purchase" in cur_loc else None,
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
    for cur_sphere in progression_data['spheres']:
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


def build_pools(all_spheres, all_pokemon, starting_acquisition_methods) -> dict[int, dict]: #TODO update to int: Pool? do we need a class for pools and/or pool entries?
    """
    Expands the Pokemon lists in each Sphere of all_spheres, then creates a dict of pools (each containing list of available Pokemon for each pool).

    args:
        all_spheres (dict of Sphere objects, where keys are numbers (int) of spheres)
        all_pokemon (dict of Pokemon objects where keys are names of Pokemon)
        starting_acquisition_methods (list of default acquisition methods from config file)

    returns:
        all_pools (dict of pools -> {pool_num: {"pool_entries": [list of pool entries], "inventory": [list of items up to this pool]}})
            example pool entry: {"pokemon_obj": Pokemon object, "acquisition_method": method (str), "acquiring_location": location name (str)}
    """
    all_pools = dict()

    # to keep track of set of items that enable evolution (stones, etc.)
    inventory = []

    # to keep track of current enabled acquisition methods that unlock Location sublists (old_rod, surf, etc.)
    enabled_acquisition_methods = [method for method in starting_acquisition_methods]

    # to keep track of spheres checked (which acquisition methods have been expanded)
    spheres_checked = {}

    # iterate over all spheres from all_spheres dict (in ascending key order)
    for sphere_num in sorted(all_spheres.keys()):

        locations = all_spheres[sphere_num].maps
        items = all_spheres[sphere_num].items
        acquisition_unlocks = all_spheres[sphere_num].acquisition_unlocks
        for item in items:
            if item not in inventory: #TODO add all dupes if we want to count how many are used?
                inventory.append(item)

        for unlock in acquisition_unlocks:
            if unlock not in enabled_acquisition_methods:
                enabled_acquisition_methods.append(unlock)

        # initialize empty list to store pokemon objects for this pool
        current_pool_entries = []

        # build list of Pokemon by iterating over each location in locations and adding all its Pokemon (the object version, from all_pokemon) to current_pool_entries
        for location_obj in locations:
            for method in enabled_acquisition_methods:
                # get list stored in that attribute (like location_obj.walk)
                method_list = getattr(location_obj, method, None)
                if method_list:
                    for pokemon in method_list:
                        pool_entry = {"pokemon_obj": all_pokemon[pokemon],
                                      "acquisition_method": method,
                                      "acquiring_location": location_obj.name}
                        current_pool_entries.append(pool_entry)

        # now also iterate over all locations from previous spheres (the ones kept track of in spheres_checked)
        # and then compare enabled_acquisition_methods at THIS point to the point in time when the previous spheres were iterated over.
        # i.e. expand all currently possible methods not yet expanded for previous spheres, and add those pokemon to this current pool as well
        for prev_sphere_num in sorted(spheres_checked.keys()):
            methods_expanded = spheres_checked[prev_sphere_num]["methods_expanded"]
            new_unlocks_to_check = [method for method in enabled_acquisition_methods if method not in methods_expanded]
            if new_unlocks_to_check:
                prev_sphere_locations = all_spheres[prev_sphere_num].maps
                # build list of Pokemon by iterating over each location in locations and adding all its Pokemon (the object version, from all_pokemon) to a list
                for prev_location_obj in prev_sphere_locations:
                    for method in new_unlocks_to_check:
                        # get list stored in that attribute (like prev_location_obj.walk)
                        method_list = getattr(prev_location_obj, method, None)
                        if method_list:
                            for pokemon in method_list:
                                pool_entry = {"pokemon_obj": all_pokemon[pokemon],
                                              "acquisition_method": method,
                                              "acquiring_location": prev_location_obj.name}
                                current_pool_entries.append(pool_entry)
                # update methods_expanded for this sphere to match current possible methods
                spheres_checked[prev_sphere_num]["methods_expanded"] += new_unlocks_to_check

        # then, current sphere "methods_expanded" list in spheres_checked dict needs to be updated so it matches the current one (so we don't do it again next iteration)
        spheres_checked[sphere_num] = {"methods_expanded": [method for method in enabled_acquisition_methods]}

        all_pools[sphere_num] = {"pool_entries": current_pool_entries, "inventory": [item for item in inventory]}

    return all_pools

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