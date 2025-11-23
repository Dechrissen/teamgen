from Core import *
from data.loader import build_all_data_structures
from ui.cli import ui_loop
#import yaml


def main():

    # validation functions should run up here (make sure all files are valid and formatted correctly)


    all_pools, all_pokemon, config_data, meta_data, global_settings, mappings, game = build_all_data_structures()

    ui_loop(all_pools, all_pokemon, config_data, meta_data, global_settings, mappings, game)

if __name__ == "__main__":
    main()