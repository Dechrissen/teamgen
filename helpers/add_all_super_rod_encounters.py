import json
import re

# --- CONFIG ---
ASM_FILE = "./pokered-data/wild/super_rod.asm"      # path to your ASM file
JSON_FILE = "./wild_red_with_all_methods.json"   # path to your JSON file
OUTPUT_FILE = "locations_red_with_super_rod.json"

def normalize_name(name):
    """Normalize names so 'ROUTE_10' matches 'Route10'."""
    return re.sub(r'[^a-z0-9]', '', name.lower())

def parse_super_rod_asm(asm_text):
    """Parse the ASM file and return {map_name: [pokemon, ...]}."""
    # Extract the map → group relationships
    map_to_group = {}
    group_pattern = re.compile(r"dbw\s+([A-Z0-9_]+),\s+\.Group(\d+)")
    for map_name, group_num in group_pattern.findall(asm_text):
        map_to_group[map_name] = f"Group{group_num}"

    # Extract all group definitions
    groups = {}
    group_def_pattern = re.compile(r"\.Group(\d+):\s+db\s+\d+([\s\S]*?)(?=\n\.Group\d+:|\Z)")
    for group_num, contents in group_def_pattern.findall(asm_text):
        pokemon_list = re.findall(r"[0-9]+,\s*([A-Z]+)", contents)
        groups[f"Group{group_num}"] = pokemon_list

    # Combine map → pokémon mapping
    final_map = {}
    for map_name, group in map_to_group.items():
        final_map[map_name] = groups.get(group, [])

    return final_map

def merge_super_rod_data(locations, super_rod_data):
    """Add super rod encounters to locations where applicable."""
    for loc in locations:
        loc_key = normalize_name(loc["map_name"])
        for asm_map, pokes in super_rod_data.items():
            if normalize_name(asm_map) == loc_key:
                loc["super_rod"] = sorted(set(pokes))
                break
    return locations

def main():
    # Read files
    with open(ASM_FILE, encoding="utf-8") as f:
        asm_text = f.read()
    with open(JSON_FILE, encoding="utf-8") as f:
        locations = json.load(f)

    # Parse and merge
    super_rod_data = parse_super_rod_asm(asm_text)
    updated_locations = merge_super_rod_data(locations, super_rod_data)

    # Write output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(updated_locations, f, indent=2)
    print(f"✅ Updated JSON written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
