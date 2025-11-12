from Pokemon import Pokemon
from Core import *
import random
import yaml

# validation functions should run up here (make sure all files are valid and formatted correctly)


# PROGRAM FLOW

# get all data #TODO change this later to all be programmatically picked from a config file which specifies which game uses which files

# get main game config data
with open('./data/gen1/config_rb.yaml') as f:
    config_data = yaml.safe_load(f)

# construct list of starting acquisition methods
starting_acquisition_methods = []
for method in config_data['acquisition_methods']:
    if method['enabled'] == True and method['default'] == True:
        starting_acquisition_methods.append(method['name'])
# config options...
prescribed_type = config_data['prescribed_type']


# construct all_pokemon
with open('./data/gen1/pokedex_rb.yaml') as f:
    pokedex_data = yaml.safe_load(f)
all_pokemon = construct_full_pokemon_set(pokedex_data)

# construct all_locations
with open('./data/gen1/locations_red.yaml') as l:
    location_data = yaml.safe_load(l)
all_locations = construct_full_location_set(location_data)

# construct all_spheres
with open('./data/gen1/progression_rb.yaml') as p:
    progression_data = yaml.safe_load(p)
all_spheres = construct_spheres(progression_data, all_locations)

# build pools from all previously constructed data
all_pools = build_pools(all_spheres, all_pokemon, starting_acquisition_methods)

# generate a test party
party = generate(all_pools, all_pokemon, prescribed_type)
for pokemon in party:
    print(pokemon.name)
