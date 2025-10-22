import json

# === CONFIG ===
LOCATION_JSON_PATH = "wild_red.json"
OUTPUT_PATH = "wild_red_with_all_methods.json"

# --- Step 1: Load JSON ---
with open(LOCATION_JSON_PATH, encoding="utf-8") as f:
    location_data = json.load(f)

# --- Step 2: Add conditional evolution_method ---
for mon in location_data:
    mon["old_rod"] = []
    mon["good_rod"] = []
    mon["super_rod"] = []
    #mon["gift"] = []
    #mon["purchase"] = []
    #mon["prize_window"] = []
    #mon["poke_flute"] = []
    #mon["fossil_restore"] = []
    #mon["static"] = []
    #mon["trade"] = []

# --- Step 3: Save updated JSON ---
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(location_data, f, indent=2)