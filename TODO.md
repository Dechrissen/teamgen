# TODO

- [ ] add a donation button, or github sponsor button (in readme?)
- post on reddit when done

- [ ] in progression yaml, figure out how to handle trade rooms as well -- when do u get access to them or how do u 
  keep track of that?
  - should they have values like "needs: onix, gets: mrmime" ?
  - probably just ignore the needed mon

- [ ] generate file for blue version when done
- [ ] generate file for solus when done

- [ ] add comments/annotations to config and other yaml files, for users
- [ ] add comments throughout code, to make sure everything is clear

- make "gift" into "choice" for HITMONs?

- [ ] add "user defined modals" to the config, which are extra modals that get added to the modal list when doing 
  the check
  - e.g. "nidoran_m and nidoran_f"
  - jynx and mr.mime

- [ ] maybe change all the stuff in the config YAML to be lists, not yaml-coded lists with booleans. Would be better 
  for future-proofing when adding more acquisition methods?


- [ ] annotate the progression file so we know where certain things come from, e.g. the moon stone on route 2 can 
  only be gotten in sphere 2, so we should have a comment "from Route2 after Cut"


- [ ] surface a "generation took X seconds" thing

- [ ] add Pool class
- [ ] ? I think the config should maybe be a Config class. This would make it easier to validate and pass along to 
  functions

- [ ] data validation tests, add "assert bst_max is int" for example so i dont have to worry about type validation in 
  the functions themselves

- [ ] Decide if adding stone evo validation


- [ ] Need a "select game" feature (or maybe this will just be in config?)
  - needs to define all relevant YAMLs to link together for X game or Y game



- [ ] add presets for enabled spheres in meta (or config) file
  - exclude_postgame (6)
  - exclude_victory_road (5 and 6)
  - johto_only
  - johto_and_kanto
  - johto_and_early_kanto

- ask chatgpt to check every location from locations is in meta spheres list