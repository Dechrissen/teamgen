from data.loader import build_all_data_structures
from ui.cli import ui_loop

def main():

    # validation functions should run up here (make sure all files are valid and formatted correctly) #TODO can we have unit tests run here?

    # build all necessary data structures
    all_pools, all_pokemon, config_data, meta_data, mappings, global_settings = build_all_data_structures()

    # run CLI UI
    ui_loop(all_pools, all_pokemon, config_data, meta_data, mappings, global_settings)

if __name__ == "__main__":
    main()