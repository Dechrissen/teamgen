import requests
import json
import time

API = "https://pokeapi.co/api/v2/"

def get_pokemon_list(limit=151):
    """Get first 151 Pokémon entries (Red/Blue/Yellow)."""
    url = API + f"pokemon?limit={limit}&offset=0"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    return data["results"]  # list of {"name": ..., "url": ...}

def get_pokemon_data(name_or_url):
    """Fetch /pokemon/{name} JSON."""
    if name_or_url.startswith("http"):
        resp = requests.get(name_or_url)
    else:
        resp = requests.get(API + f"pokemon/{name_or_url}")
    resp.raise_for_status()
    return resp.json()

def get_species_data(name_or_url):
    """Fetch /pokemon-species/{name} JSON."""
    if name_or_url.startswith("http"):
        resp = requests.get(name_or_url)
    else:
        resp = requests.get(API + f"pokemon-species/{name_or_url}")
    resp.raise_for_status()
    return resp.json()

def get_evolution_chain(url):
    """Fetch /evolution-chain/{id} JSON."""
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def flatten_evo_chain(chain_node, base_name, stage = 1, family = None, results = None):
    """
    Recursively walk the evolution chain to record stage and family.
    Returns a dict: name -> { family_line, evo_stage, is_fully_evolved }.
    """
    if results is None:
        results = {}
    if family is None:
        family = base_name

    name = chain_node["species"]["name"]
    # detect if this node has further evolves
    evolves_to = chain_node.get("evolves_to", [])
    is_fully = (len(evolves_to) == 0)

    results[name] = {
        "family_line": family,
        "evo_stage": stage,
        "is_fully_evolved": is_fully
    }
    for nxt in evolves_to:
        flatten_evo_chain(nxt, base_name, stage + 1, family, results)

    return results

def get_hm_moves_from_pokemon(poke_json):
    """
    From the Pokémon JSON, find which moves are HMs (if PokeAPI marks them).
    The PokeAPI `pokemon` JSON has a “moves” field: moves -> version_group_details.
    You may need to filter which moves are HMs via checking `move` -> `move details`.
    """
    gen1_hms = ["cut", "surf", "strength", "flash", "fly", "teleport", "dig", "softboiled"]
    hm_moves = set()
    for mv in poke_json["moves"]:
        move_name = mv["move"]["name"]
        for ver in mv["version_group_details"]:
            # version_group_details has `move_learn_method`, we want methods like “machine” or HMs
            method = ver["move_learn_method"]["name"]
            # Many HMs are under “machine” method; you can filter by move name prefix or known HM list
            if method == "machine" and move_name in gen1_hms:
                # naive filter: only include moves whose names match known HM move names
                # You’ll need a HM list map for Gen1 (e.g. “cut”, “surf”, etc.)
                hm_moves.add(move_name)
    return sorted(hm_moves)

def build_gen1_data():
    pokes = get_pokemon_list(151)
    result = []

    for entry in pokes:
        name = entry["name"]
        print("Fetching:", name)
        pjson = get_pokemon_data(name)
        species = get_species_data(name)
        # Find evolution chain
        evo_chain_url = species["evolution_chain"]["url"]
        evo_chain = get_evolution_chain(evo_chain_url)
        # the chain JSON has `chain` root
        chain_root = evo_chain["chain"]
        # base (stage 1) is chain_root["species"]["name"]
        base_name = chain_root["species"]["name"]
        evo_info = flatten_evo_chain(chain_root, base_name)

        # pick the entry for this name
        evo_entry = evo_info.get(name, {})
        family = evo_entry.get("family_line")
        stage = evo_entry.get("evo_stage")
        is_full = evo_entry.get("is_fully_evolved", False)

        # types
        types = [t["type"]["name"] for t in pjson["types"]]

        # stats sum (not Gen1-specific, but available)
        stat_total = sum(s["base_stat"] for s in pjson["stats"])

        # legendary: species JSON has a flag
        is_legend = species.get("is_legendary", False)

        # HM moves via the moves list
        hm_moves = get_hm_moves_from_pokemon(pjson)

        # assemble object
        poke_obj = {
            "name": name,
            "is_fully_evolved": is_full,
            "evo_stage": stage,
            "species_line": family,
            "types": types,
            "is_legendary": is_legend,
            "base_stat_total": 0, #stat_total,
            "hms": [""] #hm_moves
        }
        result.append(poke_obj)
        time.sleep(0.1)  # to avoid hammering the API

    return result

if __name__ == "__main__":
    data = build_gen1_data()
    with open("gen1_pokemon_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Done, wrote", len(data), "Pokémon.")