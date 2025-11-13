# TODO

- [ ] figure out how to handle trade rooms as well -- when do u get access to them or how do u keep track of that?
  - should they have values like "needs: onix, gets: mrmime" ?
  - probably just ignore the needed mon

- [ ] generate file for blue version when done

- make "gift" into "choice" for HITMONs?
- need to figure out how to limit the fossils as choices, since you pick them up as fossils

- [ ] add Pool class

- [ ] add ALL moon stones to the progression file? if so, need to add 6 of each elemental stone too.
  - otherwise we keep them just 1 each (earlier point you can acquire one)
- [ ] annotate the progression file so we know where certain things come from, e.g. the moon stone on route 2 can 
  only be gotten in sphere 2, so we should have a comment "from Route2 after Cut"
- [x] add 'items' list to pools.
  - ultimately pools should be {"pokemon": [(Pokemon, Location), (Pokemon2, Location2),...], "items": []}
  - this 'items' list will give us an easy way to check if an evo stone is in this pool, or any previous pools (during 
    generation)


- [ ] I think the config should maybe be a Config class. This would make it easier to validate and pass along to 
  functions

- [ ] fix issue where if something like dragon type is generated for pokemon 1, and 'all_share_on_type' is selected 
  along with "don't allow duplicate species", 
  then it will be stuck in an infinite loop because no other valid pokemon exist to finish the party of 6

- [ ] make sure 'blacklist' works as intended -- do we need to specify species here? just names? maybe change it to 
  "species_blacklist"?

- [ ] validation tests, add "assert bst_max is int" for example so i dont have to worry about type validation in the 
  functions themselves