## names
- finalsix
- vanillasix
- teamgen
- partygen
- uf6g (universal final six generator) or ufsg
- upg (universal party generator)
- poketeamgen
- pokesix

## Gen 3 ideas
- for gen 3, mach and acro bike selection doesnt cause issue because you can always swap them, so the pokemon generated for you in that sphere will always be gettable
- gen 3 "blacklist" where feebas is prepopulated by default


## example "build" (list and order of routes and items in file)
- or "world" ? "structure" ?
```json
"build": {
  "spheres":
    {
      "sphereNum": 1,
      "contents": [
        {"name": "Route1", "type": "map"},
        {"name":"PokeFlute", "type": "item"},
        {"name":"SuperRod", "type": "item"},
        {"name": "Surf", "type": "item"} // or "hm"?
      ]
    },
    {
      "sphereNum": 2,
      "contents": [
        ...
      ]
    }
}
```
- based on the above, the program will iterate over everything in the current sphere, add any items to "inventory", and then when it comes time to iterate over all the current maps in the sphere, it will check for inventory items to see if Super Rod entries for that map are up for grabs, if Snorlax is up for grabs based on whether poke flute is in inventory, etc.
- for each game file, in order to get the list of items to check for without hardcoding it, you can just have a quick run through the file for all the "type": "item"s from above and add all unique instances to a list. then when checking for each route, youll know which item to check for?

## what the pools look like after being generated
```json
"pools" : {
  "poolNum": 1,
  "contents": [
    "ELECTABUZZ",
    "MAGNEMITE",
    "MAGNETON",
    "PIKACHU",
    "VOLTORB"
  ],
  // this list keeps track of evo items that are available at this sphere, so the program can check all the pools to see if
  // the required evo item for the generated mon is available. it probably isnt relevant which sphere its in unless
  // you have a setting like "make sure i can get this pokemon before X point in the game"
  "evo_items": [
    "FIRE_STONE",
    "METAL_COAT"
  ]
}
```

## more ideas

- for trades in the pokemon data file: `"trade": ["ABRA for MR.MIME"]`
- add ALL moon stones separately to the logic file spheres? (in `evo_items` list)

- to be efficient with memory usage, we can use prompts in the command line after the program is already running, 
  similar to pokequiz, in order to build all the data structures (Pokemon objects etc) first, then prompt the user: 
  "Generate? Y/N" or whatever. This way it doesn't build all the data structures over and over for each run.

- option to reroll 1 pokemon (e.g. `reroll 2` to reroll the second) (to do this, we can pass an optional party list 
  of Pokemon objects to the generate_final_party function. If it's non-empty, it can be treated as the base party to 
  use/continue generating for)

- add visual graph or w/e to balance grade output
- add a region map (the one from the game) with a heatmap style overlay (or just dots) that show where your party is 
  acquired :)


## final unit tests/checks
- have a lookup table of all valid pokemon for a given region/gen, make sure all pokemon listed in the files are present in the lookup table
- validate formatting of logic file (instructions for running this should be in docs/MR instructions so contributors of new games can run the unit test first)
- the 'meta' yaml could also be used to keep track of the list of all possible items in the game? (the master list 
  source of truth to check against during unit tests?)
  - yes, via the "evolution_items_available" list
- can have test parties already built to send to the is_party_valid funciton to make sure certain ones fail (2 
  modals, etc.)
output some sort of "incompatibility" message if it detects that the 3 data YAMLs 
  are not compatible with each other (i.e. all the maps and pokemon should match spelling, etc between all 3 files 
  before any logic is run)



## idea for comparing names (str) to Location (obj) names from ChatGPT
if you want to make Location objects comparable directly by name:
You can define these methods in your class:

```class Location:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.name == other.name
        if isinstance(other, str):
            return self.name == other
        return NotImplemented

    def __hash__(self):
        return hash(self.name)
```

Then your original line would work as written:
`assert item['name'] in all_locations`
…but only do this if it makes sense in your overall design (i.e., if comparing Location to a string is a valid semantic operation in your project).


## Later ideas
- Provide ChatGPT-powered subtool in the program (CLI) that allows the user or a developer to add a new logic file for a new game by having a ChatGPT token in a config, and then a prompt with placeholders etc where the user can provide links to the prompt for ChatGPT (like links to pokemon data, locations on bulbapedia, etc) to build at least the bulk of a new logic json. Maybe in the case of romhacks, a link to the code idk.
- "get this team race" is dictated by IGT at the end of it, so it can be async.
- nickname generator function
  - pokemon universe pack
  - wacky pack
- gym leader themed generation (create pools of valid canonical pokemon from certain characters like leaders, gio, etc.)
  - then you can have a check that selects only from that pool of pokemon, OR there must be X overlap or something
  - for this mode, it might not work with the other options like BALANCED, etc. so i wonder if you just leave it 
    all as-is and let the user see if it works, or if you add in overrides to ignore the balancing for this mode
- add PNGs of all the sprites and output them with some image library
- wacky "team name assignment" feature. analyzes certain things about the pokemon (types? egg group? etc) and 
  somehow generates a name for the team from a preset pool of nouns and adjectives etc. ("the aquatic defenders"... 
  "the fiery humanoids") :/ ... idk
- add a "Team Defense" and "Team Coverage" analysis to the output, like here: https://richi3f.github.io/pokemon-team-planner
- Learn how to make a Python app work on web app --> `teamgen.app`


## Similar things
- https://richi3f.github.io/pokemon-team-planner
- https://randompokemon.com/
- https://mypokemonteam.com/