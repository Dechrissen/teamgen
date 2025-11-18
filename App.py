from Pokemon import Pokemon
from Core import *
import random
import yaml

# validation functions should run up here (make sure all files are valid and formatted correctly)

# GET ALL DATA #TODO change this later to all be programmatically picked from a config file which specifies which game uses which files

# get game config data
with open('./data/gen1/config_rb.yaml') as f:
    config_data = yaml.safe_load(f)

# get game meta data
with open('./data/gen1/meta_rb.yaml') as m:
    meta_data = yaml.safe_load(m)

# construct list of starting acquisition methods
starting_acquisition_methods = []
for method in meta_data['acquisition_methods']:
    # add each acquisition method to the list of starting methods if it's both default (in metadata) and True (in allowed list in config data)
    if method['is_default'] == True and config_data['allowed_acquisition_methods'][method['name']] == True:
        starting_acquisition_methods.append(method['name'])



# construct all_pokemon
with open('./data/gen1/pokedex_rb.yaml') as f:
    pokedex_data = yaml.safe_load(f)
all_pokemon = construct_full_pokemon_set(pokedex_data)

# construct all_locations
with open('./data/gen1/locations_red.yaml') as l:
    location_data = yaml.safe_load(l)
all_locations = construct_full_location_set(location_data)

# construct all_spheres
# with open('./data/gen1/progression_rb.yaml') as p:
#     progression_data = yaml.safe_load(p)
all_spheres = construct_spheres(meta_data, all_locations)

# build pools from all previously constructed data
all_pools = build_pools(all_spheres, all_pokemon, starting_acquisition_methods)



# TESTING
# for entry in all_pools[5]['pool_entries']:
#     print("acquire", entry["pokemon_obj"].name, "by", entry["acquisition_method"], "at", entry["acquiring_location"])

# print(all_pools[1]['inventory'])
# print(all_pools[2]['inventory'])


# MAIN
print("Generating party...")
party = generate_final_party(all_pools, all_pokemon, config_data, meta_data, n=6)
for pokemon in party:
    print(pokemon.name)