import os
import re
import json

# === CONFIG ===
ASM_DIR = "./pokered-data/base_stats"
POKEMON_JSON_PATH = "gen1_pokemon_data_with_hms.json"
OUTPUT_PATH = "gen1_pokemon_data_with_hms_and_bst.json"

# Regex patterns
pokedex_pattern = re.compile(r"db\s+DEX_([A-Z0-9_]+)")
# Example: db  25,  20,  15,  90, 105
stats_pattern = re.compile(r"db\s+(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)")

base_stat_totals = {}

# --- Step 1: Extract base stats from each asm file ---
for filename in os.listdir(ASM_DIR):
    if not filename.endswith(".asm"):
        continue

    with open(os.path.join(ASM_DIR, filename), encoding="utf-8") as f:
        content = f.read()

    # Find Pokémon name
    dex_match = pokedex_pattern.search(content)
    if not dex_match:
        continue
    pokemon_name = dex_match.group(1).lower()

    # Find base stats
    stats_match = stats_pattern.search(content)
    if stats_match:
        stats = list(map(int, stats_match.groups()))
        total = sum(stats)
        base_stat_totals[pokemon_name] = total

# --- Step 2: Read existing JSON ---
with open(POKEMON_JSON_PATH, encoding="utf-8") as f:
    pokemon_data = json.load(f)

# --- Step 3: Update base_stat_total field ---
for mon in pokemon_data:
    name = mon["name"].lower()
    if name in base_stat_totals:
        mon["base_stat_total"] = base_stat_totals[name]

# --- Step 4: Write updated JSON ---
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(pokemon_data, f, indent=2)