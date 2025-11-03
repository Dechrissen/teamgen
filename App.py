from Pokemon import Pokemon
from Core import *
import random
import yaml

with open('./data/gen1/pokedex_rb.yaml') as f:
    pokedex_data = yaml.safe_load(f)
all_pokemon = construct_full_pokemon_set(pokedex_data)
rand_key=random.choice(list(all_pokemon.keys()))
rand_mon = all_pokemon[rand_key]
print(rand_mon.name, rand_mon.types)

# test getting child
print(get_immediate_child_mon(rand_mon, all_pokemon).name)


with open('./data/gen1/locations_red.yaml') as l:
    location_data = yaml.safe_load(l)
all_locations = construct_full_location_set(location_data)
# rand_location = random.choice(list(all_locations))
# print(rand_location.name, rand_location.trade)


with open('./data/gen1/progression_rb.yaml') as p:
    progression_data = yaml.safe_load(p)

# all_spheres = construct_spheres(progression_data, all_locations)
#
# for sphere_num in all_spheres.keys():
#     print(sphere_num, "maps:", all_spheres[sphere_num].maps, "items:", all_spheres[sphere_num].items)

#print(progression_data)







#print(pokedex_data[27])

#test_mon = Pokemon('charmander', 'charmander', 1, False, False, ['fire'], 100, ['CUT'], 'none')
#print(test_mon.name, test_mon.types, test_mon.hm_learnset, test_mon.bst)
