## names
- finalsix
- vanillasix
- teamgen
- partygen
- uf6g (universal final six generator) or ufsg
- upg (universal party generator)
- poketeamgen
- pokesix

## General ideas
- kanto.yaml, region map file that stores kanto location data
    - list of all valid pokemon locations (routes, but also game corner, gift pokemon spots)
    - list of field move blockages preventing access to each one, somehow
- then in the game files, e.g. vanilla_red.yaml or w/e, each pokemon listed needs to have a location list
    - locations: [route_1, game_corner, cinnabar_lab] but they all need to match the format used in the region file
    - a check should run before any generation to check whether all game files use valid locations, etc, and error message should print nicely explaining the errors if any
- for gen 3, mach and acro bike selection doesnt cause issue because you can always swap them, so the pokemon generated for you in that sphere will always be gettable
- "exclude feebas" option
  - or a list of "pokemon_to_exclude" where feebas is prepopulated by default
- "don't use starter" option
  - maybe if this is selected, ignore sector 1 generated mon
- "make sure final party can use XYZ HMs"
- "dont use pokemon that evolve by trade"
- "dont use gift pokemon or trade pokemon"
- generation mode should be "balanced" by default, ensuring generation of at least 1/2 pokemon in sector 1, otherwise player will be waiting for a while till they can get their first mon
  - other options include "ignore sector 1" or w/e, and "late game heavy"
- in order to handle Snorlax and different rods, etc, we can keep track of which spheres we've currently unlocked (and thus which routes are available to generate from) 
- for the unit tests, they should output some sort of "incompatibility" message if it detects that the 3 data YAMLs 
  are not compatible with each other (i.e. all the maps and pokemon should match spelling, etc between all 3 files 
  before any logic is run)


## Things I will need
- logic files (region layout/grid json or yaml)
    - only need to go as deep as pokemon/required items (hms, stones) are located, e.g. trader house, game corner, silph co, dept store
- pokemon data (hms learned, evolution methods, location found, acquisition method like gift-trade-wild)
- traversal code (the code that steps through the region)
- player state (hms, evolution items, pokemon in party)
- a variable to hold "starting location" for the player so i can test generation from midpoints like saffron to test the Lapras thing etc.
    - might need to encode "events" that have been completed? to get into Silph Co building etc.
        - really dont want to though, would rather keep it simple

When your traversal function reaches a new location:
1. Add any newly obtainable items to your “inventory”.
2. Check which Pokémon in your team can evolve with those items.
3. Apply the evolution immediately (if you want realistic progression).

## example map file (old, for super logical version)
```json
"locations": {
    "Route 1": {
      "connections": [
        { "to": "Pallet Town", "requires": [] },
        { "to": "Viridian City", "requires": [] }
      ],
      "pokemon": {
        "wild": ["Pidgey", "Rattata"],
        "gift": [],
        "trade": []
      },
      "items": []
    },
    ...
}
```

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
- the program should probably generate all the spheres from the config file, then generate a party (final evo_stages first?), and check it against the spheres. if it cant find the final form of a pokemon in a sphere, step down to the previous stage and check for it in the wild?
- for trades in the pokemon data file: `"trade": ["ABRA for MR.MIME"]`
- add ALL moon stones separately to the logic file spheres? (in `evo_items` list)
- since the program will probably generate a final 6 first (all with final stages) then there should prob be an initial step where it iterates over all pokemon and makes a pool of "full evolved" mons and only considers those to generate
- every time an evolution item is found in a sphere during iteration, it can just be added to the 'inventory'. if an evo item is needed for evolution in any of the generated pokemon, it will just check the inventory to see if it's there (or if there's enough)
- for hitmons/fossils, maybe have a list in the progression_red.yaml file that says which pokemon should be considered modal for that game. So it doesn't matter whether the fossils are available once or a second time in victory road (solus), or same for hitmons, it's up to the discretion of the yaml creator to say what makes sense as modal.
- getParent() and getChild() in the Pokemon class? how will it access all the other Pokemon objects to check for this?
- to be efficient with memory usage, we can use prompts in the command line after the program is already running, 
  similar to pokequiz, in order to build all the data structures (Pokemon objects etc) first, then prompt the user: 
  "Generate? Y/N" or whatever. This way it doesn't build all the data structures over and over for each run.

## final unit tests/checks
- have a lookup table of all valid pokemon for a given region/gen, make sure all pokemon listed in the files are present in the lookup table
- validate formatting of logic file (instructions for running this should be in docs/MR instructions so contributors of new games can run the unit test first)


  when you have access to Surf (badge + HM) not just the HM item itself


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