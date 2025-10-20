# helper script for building the gen 1 vanilla game files

import re
import glob
import json

def parse_wildmons(filepath):
    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    # Extract route name from label
    route_match = re.search(r'(\w+)WildMons:', text)
    route = route_match.group(1) if route_match else filepath

    def extract_pokemon(section_text):
        """
        Return dict {'RED': set(), 'BLUE': set()} for the given text section.
        Logic:
         - remove all IF...ENDC blocks and treat the remainder as shared (apply to both).
         - parse IF DEF(_RED) ... ELIF DEF(_BLUE) ... ENDC blocks (if any).
         - parse standalone IF DEF(_RED) ... ENDC and IF DEF(_BLUE) ... ENDC blocks too.
        """
        results = {"RED": set(), "BLUE": set()}

        # 1) Shared mons: remove any IF...ENDC blocks, then parse remaining 'db' entries.
        shared_text = re.sub(r'IF DEF\(_(?:RED|BLUE)\)[\s\S]*?ENDC', '', section_text)
        shared_mons = re.findall(r'db\s+\d+,\s*([A-Z0-9_]+)', shared_text)
        results["RED"].update(shared_mons)
        results["BLUE"].update(shared_mons)

        # 2) Handle IF DEF(_RED) ... ELIF DEF(_BLUE) ... ENDC (paired form)
        paired_pattern = re.compile(
            r'IF DEF\(_RED\)([\s\S]*?)ELIF DEF\(_BLUE\)([\s\S]*?)ENDC',
            flags=re.MULTILINE
        )
        for m in paired_pattern.finditer(section_text):
            red_block, blue_block = m.group(1), m.group(2)
            results["RED"].update(re.findall(r'db\s+\d+,\s*([A-Z0-9_]+)', red_block))
            results["BLUE"].update(re.findall(r'db\s+\d+,\s*([A-Z0-9_]+)', blue_block))

        # 3) Handle IF DEF(_RED) ... ENDC (standalone, not paired with ELIF)
        red_only_pattern = re.compile(r'IF DEF\(_RED\)([\s\S]*?)ENDC', flags=re.MULTILINE)
        for m in red_only_pattern.finditer(section_text):
            block = m.group(1)
            # skip if it's the paired form already handled (paired regex captured ELIF)
            if re.search(r'ELIF DEF\(_BLUE\)', block):
                continue
            results["RED"].update(re.findall(r'db\s+\d+,\s*([A-Z0-9_]+)', block))

        # 4) Handle IF DEF(_BLUE) ... ENDC (standalone)
        blue_only_pattern = re.compile(r'IF DEF\(_BLUE\)([\s\S]*?)ENDC', flags=re.MULTILINE)
        for m in blue_only_pattern.finditer(section_text):
            block = m.group(1)
            # skip if it was already captured by paired pattern (shouldn't be)
            if re.search(r'ELIF DEF\(_RED\)', block):
                continue
            results["BLUE"].update(re.findall(r'db\s+\d+,\s*([A-Z0-9_]+)', block))

        return results

    # --- Grass ---
    grass_section = text.split('end_grass_wildmons')[0]
    grass = extract_pokemon(grass_section)

    # --- Water ---
    water_section_match = re.search(r'def_water_wildmons[\s\S]*?end_water_wildmons', text)
    water_text = water_section_match.group(0) if water_section_match else ""
    water = extract_pokemon(water_text)

    return {
        "route": route,
        "RED": {
            "grass": sorted(grass["RED"]),
            "water": sorted(water["RED"])
        },
        "BLUE": {
            "grass": sorted(grass["BLUE"]),
            "water": sorted(water["BLUE"])
        }
    }

if __name__ == "__main__":
    all_data_red, all_data_blue = [], []

    for file in glob.glob("pokered-data/wild/maps/*.asm"):
        parsed = parse_wildmons(file)
        all_data_red.append({
            "route": parsed["route"],
            "grass": parsed["RED"]["grass"],
            "water": parsed["RED"]["water"]
        })
        all_data_blue.append({
            "route": parsed["route"],
            "grass": parsed["BLUE"]["grass"],
            "water": parsed["BLUE"]["water"]
        })

    # sort the routes so they're alphabetical in the output json
    all_data_red = sorted(all_data_red, key=lambda x: x["route"].lower())
    all_data_blue = sorted(all_data_blue, key=lambda x: x["route"].lower())

    with open("wild_red.json", "w", encoding="utf-8") as f:
        json.dump(all_data_red, f, indent=2)
    with open("wild_blue.json", "w", encoding="utf-8") as f:
        json.dump(all_data_blue, f, indent=2)

    print(f"✅ Parsed {len(all_data_red)} routes → wild_red.json & wild_blue.json (sorted alphabetically)")

