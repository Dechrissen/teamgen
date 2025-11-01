# functions needed

# - iterate over all spheres in the prog file and expand each map, add respective pokemon to a group for each sphere, and items to inventory for each sphere
# - 

from Pokemon import *
from Location import *
from Sphere import Sphere


def construct_full_pokemon_set(pokedex_data) -> set[Pokemon]:
    """
    Creates a set of all Pokémon from an input pokedex YAML.

    args:
        pokedex_data (list of dicts, one for each mon)

    returns:
        all_pokemon (set of Pokemon objects)
    """
    # create empty set
    all_pokemon = set()

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
        
        # add current mon's Pokemon object to full set
        all_pokemon.add(cur_mon_obj)

    return all_pokemon

def construct_full_location_set(location_data) -> set[Location]:
    """
        Creates a set of all Locations from an input locations YAML.

        args:
            location_data (list of dicts, one for each location)

        returns:
            all_locations (set of Location objects)
        """
    # create empty set
    all_locations = set()

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

        # add current loc's Location object to full set
        all_locations.add(cur_loc_obj)

    return all_locations

def construct_spheres(progression_data) -> dict:
    """
        Creates a set of all Spheres from an input progression YAML.
    """
    # probably ultimately create a dict of spheres, where the keys correspond to sphere number (int) and the value is the rest of the sphere info in a Sphere object

    # create empty set
    all_spheres = dict()


    for cur_sphere in progression_data['world']['spheres']:
        sphereNum = cur_sphere['sphereNum']
        sphereContents = cur_sphere['contents']
        maps, items = [], []

        for element in sphereContents:
            if element['type'] == 'map':
                maps.append(element['name'])
            elif element['type'] == 'item':
                items.append(element['name'])

        all_spheres[sphereNum] = Sphere(maps, items)

    return all_spheres

def test_whether_locations_are_all_valid_in_progression_file(all_locations):
    """
        unfinished
    """
    # source of truth for assert statement below
    location_names = {loc.name for loc in all_locations}
    for item in sphereContents:
        print(item['name'])
        assert item['name'] in location_names

    return