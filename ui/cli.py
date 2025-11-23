import os
from Core import *

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display_party(party_blob, config_data):
    # ANSI codes
    TITLE = "\033[30m\033[103m" # black text, bright yellow background
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_MAGENTA = "\033[95m"
    RESET = "\033[0m"

    print(f"{TITLE}===== TeamGen ====={RESET}\n")

    # Case 1: Never generated yet
    if party_blob is None:
        print("Welcome to TeamGen!\n")
        return

    # Case 2: Tried but failed
    if party_blob is False:
        print("No party could be generated with current settings!\n")
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

def ui_loop(all_pools, all_pokemon, config_data, meta_data):
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

        display_party(party_on_screen, config_data)

        print(f"{BRIGHT_CYAN}ENTER{RESET} - Generate")
        print(f"{BRIGHT_CYAN}R{RESET} - Random mode")
        print(f"{BRIGHT_CYAN}Q{RESET} - Quit")
        print("")
        user = input().strip().lower()

        if user == "q":
            return
        if user == "r":
            mode='full_randomizer'

        # when ENTER pressed → generate new party
        if DEBUG:
            pass
        else:
            clear()
        print("Generating party...\n")

        if mode == 'full_randomizer':
            party_blob = generate_fully_randomized_party(all_pokemon, n=6)
        else:
            party_blob = generate_final_party(
                all_pools, all_pokemon, config_data, meta_data, n=6
            )

        # if generation fails, mark explicitly with False
        if party_blob is None:
            party_on_screen = False
        else:
            party_on_screen = party_blob
