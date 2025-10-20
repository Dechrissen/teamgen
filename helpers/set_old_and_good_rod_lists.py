import json

# --- CONFIG ---
INPUT_FILE = "locations_red_with_super_rod.json"          # your input file
OUTPUT_FILE = "locations_red_with_correct_rods.json" # output file

def update_fishing_data(locations):
    for loc in locations:
        if not loc.get("super_rod"):  # if empty list
            # remove all three keys
            loc.pop("old_rod", None)
            loc.pop("good_rod", None)
            loc.pop("super_rod", None)
        else:
            # ensure these exist and have proper values
            loc["old_rod"] = ["MAGIKARP"]
            loc["good_rod"] = ["GOLDEEN", "POLIWAG"]
    return locations

def main():
    with open(INPUT_FILE, encoding="utf-8") as f:
        locations = json.load(f)

    updated = update_fishing_data(locations)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(updated, f, indent=2)
    print(f"✅ Updated locations written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
