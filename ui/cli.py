import os
from Core import *
from data.loader import build_all_data_structures
import yaml

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def set_game(mappings):
    selected_game = None
    valid_options = {}

    for i, game_title in enumerate(mappings.keys(), start=1):
        valid_options[str(i)] = game_title
        print(f"{i}. {game_title}")

    print("")
    print("Select a game by number.\n")

    user = input().strip().lower()

    if user not in valid_options.keys():
        print("not valid")
        return False
    else:
        print("valid")
        selected_game = valid_options[user]
        print(f"selected game is {selected_game} with mappings {mappings[selected_game]}")
        with open("./config/global_settings.yaml", "r") as f:
            data = yaml.safe_load(f)
        data["game"] = selected_game
        with open("config/global_settings.yaml", "w") as f:
            yaml.safe_dump(data, f)
        return True

def display_party(party_blob, config_data, game):
    # ANSI codes
    TITLE = "\033[30m\033[103m" # black text, bright yellow background
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_RED = "\033[91m"
    RESET = "\033[0m"

    print(f"{TITLE}===== TeamGen ====={RESET}\n")

    print(f"Game: {game}\n")

    # Case 1: Never generated yet, or set_game invalid option was passed
    if party_blob is None:
        print("Welcome to TeamGen!\n")
        return

    # Case 2: Tried but failed
    if party_blob is False:
        print("No party could be generated with current settings!\n")
        return

    if party_blob == 'invalid_input':
        print(f"{BRIGHT_RED}Invalid input! Please try again.{RESET}\n")
        return

    # print Pokemon
    for i, pokemon in enumerate(party_blob["party_with_acquisition_data"], start=1):
        prescription_details = ""
        if config_data['show_acquisition_details']:
            prescribed_pool_entry = pokemon["random_pool_entry_instance"]
            # need to check if it's not None, because it can be None if `full_randomizer` mode is used
            if prescribed_pool_entry is not None:
                prescribed_acquisition_method = prescribed_pool_entry["acquisition_method"] if prescribed_pool_entry else None
                prescribed_acquiring_location = prescribed_pool_entry["acquiring_location"] if prescribed_pool_entry else None
                earliest_form = pokemon["earliest_form"]
                earliest_pool = pokemon["earliest_pool"]
                prescription_details = f" - acquire as {earliest_form.name} via {prescribed_acquisition_method} at {prescribed_acquiring_location} (Sphere {earliest_pool})"
        print(f"{BRIGHT_MAGENTA}{i}.{RESET} {pokemon['party_member_obj'].name}" + prescription_details)

    if config_data['show_balance_stats']:
        print(f"\n{BRIGHT_GREEN}------ STATS ------{RESET}")
        print("party_distribution:", party_blob["party_distribution"])
        print("score_median:", party_blob["score_median"])
        print("lean:", party_blob["lean"])
        print("spread:", party_blob["spread"])
        print("pattern:", party_blob["pattern"])

    print()

def ui_loop(all_pools, all_pokemon, config_data, meta_data, global_settings, mappings, game):


    # ANSI codes
    GREEN = "\033[32m"
    BRIGHT_CYAN = "\033[96m"
    RESET = "\033[0m"

    party_on_screen = None

    while True:
        if DEBUG:
            # so we don't clear the screen and can see debug output
            pass
        else:
            clear()

        mode = None

        display_party(party_on_screen, config_data, game)

        print(f"Press {BRIGHT_CYAN}ENTER{RESET} to generate a party.")
        print(f"{BRIGHT_CYAN}R{RESET} - Random generation")
        print(f"{BRIGHT_CYAN}S{RESET} - Set game")
        print(f"{BRIGHT_CYAN}Q{RESET} - Quit")
        print("")
        user = input().strip().lower()

        if user == "q":
            print("Goodbye!")
            return
        if user == "s":
            mode = "set_game"
        if user == "r":
            mode='full_randomizer'

        # when ENTER pressed → generate new party
        if DEBUG:
            pass
        else:
            clear()


        if mode == 'full_randomizer':
            print("Generating party...\n")
            party_blob = generate_fully_randomized_party(all_pokemon, n=6)
        elif mode == 'set_game':
            if set_game(mappings):
                all_pools, all_pokemon, config_data, meta_data, global_settings, mappings, game = build_all_data_structures()
                party_on_screen = None
                continue
            else:
                party_on_screen = 'invalid_input'
                continue
        else:
            print("Generating party...\n")
            party_blob = generate_final_party(
                all_pools, all_pokemon, config_data, meta_data, n=6
            )

        # if generation fails, mark explicitly with False
        if party_blob is None:
            party_on_screen = False
        else:
            party_on_screen = party_blob
