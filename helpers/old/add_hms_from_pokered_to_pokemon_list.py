import os
import re
import json

# === CONFIG ===
ASM_DIR = "./pokered-data/base_stats"
POKEMON_JSON_PATH = "gen1_pokemon_data.json"
OUTPUT_PATH = "gen1_pokemon_data_with_hms.json"

# HMs/TMs of interest
TARGET_MOVES = {"CUT", "SURF", "STRENGTH", "FLY", "FLASH", "DIG", "SOFTBOILED", "TELEPORT"}

# Regex patterns
pokedex_pattern = re.compile(r"db\s+DEX_([A-Z0-9_]+)")
tmhm_pattern = re.compile(r"tmhm\s+(.+)", re.DOTALL)

# --- Step 1: extract HMs from .asm files ---
hm_dict = {}

for filename in os.listdir(ASM_DIR):
    if not filename.endswith(".asm"):
        continue

    with open(os.path.join(ASM_DIR, filename), encoding="utf-8") as f:
        content = f.read()

    dex_match = pokedex_pattern.search(content)
    if not dex_match:
        continue
    pokemon_name = dex_match.group(1).lower()  # lowercase to match JSON

    tmhm_match = tmhm_pattern.search(content)
    if tmhm_match:
        tmhm_block = tmhm_match.group(1)
        tmhm_block = re.sub(r";.*", "", tmhm_block)  # strip comments
        tmhm_block = tmhm_block.replace("\\", " ")
        moves = re.findall(r"\b[A-Z_]+\b", tmhm_block)
        learned_hms = [m for m in moves if m in TARGET_MOVES]
        if learned_hms:
            hm_dict[pokemon_name] = learned_hms

# --- Step 2: read your existing Pokémon JSON ---
with open(POKEMON_JSON_PATH, encoding="utf-8") as f:
    pokemon_data = json.load(f)

# --- Step 3: update hms field where applicable ---
for mon in pokemon_data:
    name = mon["name"].lower()
    if name in hm_dict:
        mon["hms"] = hm_dict[name]
    elif mon.get("hms") == [""]:
        mon["hms"] = []  # clean up placeholder empty string

# --- Step 4: write updated JSON ---
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(pokemon_data, f, indent=2)