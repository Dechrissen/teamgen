import json

# === CONFIG ===
POKEMON_JSON_PATH = "gen1_pokemon_data_with_hms_and_bst.json"
OUTPUT_PATH = "gen1_pokemon_data_with_hms_bst_evomethod.json"

# --- Step 1: Load JSON ---
with open(POKEMON_JSON_PATH, encoding="utf-8") as f:
    pokemon_data = json.load(f)

# --- Step 2: Add conditional evolution_method ---
for mon in pokemon_data:
    evo_stage = mon.get("evo_stage", 0)
    if evo_stage in (1, 2):
        mon["evolution_method"] = "level-up"
    else:
        mon["evolution_method"] = "none"

# --- Step 3: Save updated JSON ---
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(pokemon_data, f, indent=2)