# TODO

- [ ] add a donation button, or github sponsor button (in readme?)
- post on reddit when done

- add version to teamgen header (pull from python package file/info? is this a thing?)

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

- [ ] Proper unit test suite

- [ ] add Pool class
- [ ] ? I think the config should maybe be a Config class. This would make it easier to validate and pass along to 
  functions

- [ ] YAML data validation tests, add "assert bst_max is int" for example so i dont have to worry about type 
  validation in 
  the functions themselves

- [ ] Decide if adding stone evo validation

- [ ] order output by sphere, ascending
  - add special check 'if starter, always put in slot 1'
  - but everything else doesn't matter, just sphere order

- [ ] Should the 'output acquisition data/balance stats' options be in the global_settings yaml?
  - maybe add a mode 'o' for output to change these in the CLI UI


- ask chatgpt to check every location from locations is in meta spheres list