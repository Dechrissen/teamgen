# TODO

- add a donation button, or github sponsor button (in readme)
- make a logo
- add to itch.io

- add to website/linkedin/portfolio/solus webpage

- make sure push for first release has "recommended settings" in config files
- test on actual linux

- add Yellow

- figure out how to handle trade rooms
  - should they have values like "needs: onix, gets: mrmime" ?
  - probably just ignore the needed mon

- clean up CLI UI code and add some comments

- add comments to unit test functions

- make "gift" into "choice" for HITMONs?

- add "user defined modals" to the config, which are extra modals that get added to the modal list when doing the check
  - e.g. "nidoran_m and nidoran_f"
  - jynx and mr.mime

- annotate the progression file so we know where certain things come from, e.g. the moon stone on route 2 can only be gotten in sphere 2, so we should have a comment "from Route2 after Cut"

- Proper unit test suite

- add Pool class
- config should maybe be a Config class. This would make it easier to validate and pass along to functions

- Decide if adding stone evo validation

- add HM coverage output
  - list of HMs, check marks next to covered ones, or color them green

- check every location from locations is in meta spheres list (also add unit test for this?)

- add CONTRIBUTING.md with guidelines for adding data files for additional games

- add unit tests for party generation functions (define test parties)

- add toggle options for "Show balance stats" and "Show acquisition details" in UI

- add 'export to txt' option for saving teams, or do it automatically (last X teams generated in a file)
- ~~fix VENUSAUR having either "acquire via walk at ViridianForest" OR the normal starter method for Solus RGB when 
  force_starter = True, while the 
  other 2 starters correctly have their "starter" method selected.~~