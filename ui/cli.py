import os
from Core import *

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display_party(party_blob):
    #RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    print(f"{YELLOW}===== TeamGen ====={RESET}\n")

    if not party_blob:
        print("No party.\n")
        return

    # 6 Pokemon names
    for i, pokemon in enumerate(party_blob["party_with_acquisition_data"], start=1):
        print(f"{GREEN}{i}. {pokemon['party_member_obj'].name}{RESET}")

    print("\n--- Stats ---")
    print("party_distribution:", party_blob["party_distribution"])
    print("score_median:", party_blob["score_median"])
    print("lean:", party_blob["lean"])
    print("spread:", party_blob["spread"])
    print("pattern:", party_blob["pattern"])
    print()

def ui_loop(all_pools, all_pokemon, config_data, meta_data):

    party_on_screen = None

    while True:
        if DEBUG:
            pass
        else:
            clear()

        display_party(party_on_screen)

        print("Press ENTER to generate a new party, or Q to quit.")
        user = input().strip().lower()

        if user == "q":
            return

        # ENTER → generate new party
        if DEBUG:
            pass
        else:
            clear()
        print("Generating party...\n")

        party_blob = generate_final_party(
            all_pools, all_pokemon, config_data, meta_data, n=6
        )

        party_on_screen = party_blob
