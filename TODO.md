# TODO

- [ ] in progression yaml, figure out how to handle trade rooms as well -- when do u get access to them or how do u 
  keep track of that?
  - should they have values like "needs: onix, gets: mrmime" ?
  - probably just ignore the needed mon

- [ ] generate file for blue version when done
- [ ] generate file for solus when done

- [ ] add comments/annotations to config and other yaml files, for users

- make "gift" into "choice" for HITMONs?


- [ ] maybe change all the stuff in the config YAML to be lists, not yaml-coded lists with booleans. Would be better 
  for future-proofing when adding more acquisition methods?


- [ ] annotate the progression file so we know where certain things come from, e.g. the moon stone on route 2 can 
  only be gotten in sphere 2, so we should have a comment "from Route2 after Cut"


- [ ] add Pool class
- [ ] ? I think the config should maybe be a Config class. This would make it easier to validate and pass along to 
  functions


- [ ] data validation tests, add "assert bst_max is int" for example so i dont have to worry about type validation in 
  the functions themselves



- [ ] add a bunch of debug print statements and a DEBUG variable
  - if DEBUG and condition:
    - print...

- [ ] Ultimately need one big blob of final output data from which to pull for visual printed output
  - party members
  - associated locations with acquisition method
  - party distribution
  - balancing/spread/pattern
  then based on a CONFIG (of what is wanted in the output, e.g. 'show_prescribed_locations' and 
    'show_acquisition_methods' etc.) we can print the final output.