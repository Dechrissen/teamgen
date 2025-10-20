import json
from collections import defaultdict

# === CONFIG ===
POKEMON_JSON_PATH = "gen1_pokemon_data_with_hms_bst_evomethod.json"
OUTPUT_PATH = "gen1_pokemon_data_with_hms_bst_evomethod_fixed.json"

# --- Step 1: Load JSON ---
with open(POKEMON_JSON_PATH, encoding="utf-8") as f:
    pokemon_data = json.load(f)

# --- Step 2: Group Pokémon by species_line ---
species_groups = defaultdict(list)
for mon in pokemon_data:
    species_groups[mon["species_line"]].append(mon)

# --- Step 3: Process each family line ---
for family, mons in species_groups.items():
    # Sort by evo_stage
    mons.sort(key=lambda m: m.get("evo_stage", 0))

    # Collect their current evolution methods
    evo_methods = [m.get("evolution_method", "none") for m in mons]

    # Shift the methods up one stage
    shifted_methods = ["none"] + evo_methods[:-1]

    # Assign new field and remove old one
    for mon, new_method in zip(mons, shifted_methods):
        mon["evolution_method_required"] = new_method
        if "evolution_method" in mon:
            del mon["evolution_method"]

# --- Step 4: Ensure stage 1 Pokémon always say "none" ---
for mon in pokemon_data:
    if mon.get("evo_stage") == 1:
        mon["evolution_method_required"] = "none"

# --- Step 5: Save updated JSON ---
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(pokemon_data, f, indent=2)