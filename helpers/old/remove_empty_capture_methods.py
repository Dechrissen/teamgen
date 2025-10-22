import json

# --- CONFIG ---
INPUT_FILE = "locations_red_with_correct_rods.json"          # input file
OUTPUT_FILE = "locations_red.json" # output file

CAPTURE_METHODS = {"walk", "surf", "old_rod", "good_rod", "super_rod"}

def clean_locations(locations):
    for loc in locations:
        # iterate over the capture methods and remove if empty or null
        for method in list(loc.keys()):
            if method in CAPTURE_METHODS:
                val = loc[method]
                if not val:  # catches [], None, ""
                    loc.pop(method)
    return locations

def main():
    with open(INPUT_FILE, encoding="utf-8") as f:
        locations = json.load(f)

    cleaned = clean_locations(locations)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2)
    print(f"✅ Cleaned locations written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
