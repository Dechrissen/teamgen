from Pokemon import Pokemon
from Functions import *
import random
import yaml

with open('./data/gen1/pokedex_rb.yaml') as f:
    pokedex_data = yaml.safe_load(f)

all_pokemon = constructFullPokemonSet(pokedex_data)

rand_mon=random.choice(list(all_pokemon))



print(rand_mon.name, rand_mon.types)




#print(pokedex_data[27])

#test_mon = Pokemon('charmander', 'charmander', 1, False, False, ['fire'], 100, ['CUT'], 'none')
#print(test_mon.name, test_mon.types, test_mon.hm_learnset, test_mon.bst)