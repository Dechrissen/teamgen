# functions needed
# - iterate over all pokemon in the pokedex file and return a list/dict of all pokemon available
# - iterate over all spheres in the prog file and expand each map, add respective pokemon to a group for each sphere, and items to inventory for each sphere
# - 

from Pokemon import *


def constructFullPokemonSet(pokedex_data) -> set[Pokemon]:
    '''
    Creates a set of all Pokémon from an input pokedex YAML.

    args:
        pokedex_data (list of dicts, one for each mon)

    returns:
        all_pokemon (set of Pokemon objects)
    '''
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
        
        # add current mon Pokemon object to full set
        all_pokemon.add(cur_mon_obj)

    return all_pokemon