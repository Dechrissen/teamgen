# TODO

- [ ] in progression yaml, figure out how to handle trade rooms as well -- when do u get access to them or how do u 
  keep track of that?
  - should they have values like "needs: onix, gets: mrmime" ?
  - probably just ignore the needed mon

- [ ] generate file for blue version when done
- [ ] generate file for solus when done

- [ ] add comments/annotations to config and other yaml files, at least titles

- make "gift" into "choice" for HITMONs?
- need to figure out how to limit the fossils as choices, since you pick them up as fossils

- [ ] maybe change all the stuff in the config YAML to be lists, not yaml-coded lists with booleans. Would be better 
  for future-proofing when adding more acquisition methods?

- [ ] add ALL moon stones to the progression file? if so, need to add 6 of each elemental stone too.
  - otherwise we keep them just 1 each (earliest point you can acquire one)
- [ ] annotate the progression file so we know where certain things come from, e.g. the moon stone on route 2 can 
  only be gotten in sphere 2, so we should have a comment "from Route2 after Cut"


- [ ] add Pool class
- [ ] ? I think the config should maybe be a Config class. This would make it easier to validate and pass along to 
  functions

- [ ] fix issue where if something like dragon type is generated for pokemon 1, and 'all_share_one_type' is selected 
  along with "don't allow duplicate species", 
  then it will be stuck in an infinite loop because no other valid pokemon exist to finish the party of 6


- [ ] validation tests, add "assert bst_max is int" for example so i dont have to worry about type validation in the 
  functions themselves

- [ ] is_party_viable function should actually ANALYZE the viablity of a party and assign it a grade.
  - BALANCED
  - LATE_GAME_HEAVY
  - EARLY_GAME_HEAVY
  - etc
  - THEN, you can also have config options to select a certain grade, or ALLOW_ANY

- [ ] add time / tries / progress text
  - Print "Generating party..."
  - initialize time variable at the start of the program
  - pass it along to all? functions
  - if time is taking too long, probably means 6th party member can't be found (or some other config options 
    preventing party from being built) -> reset time and try again (and increment "tries")
  - if tries > 10, probably means party doesn't exist, so return "Party can't be found"

- [ ] Do we need to keep track of static/purchase/trade pokemon being limited to only 1 per game? even if 
  allow_duplicate species is on, it shouldnt generate >1 of these.