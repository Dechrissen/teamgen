import pytest
from conftest import load_yaml

def filter_yaml(yaml_files, category):
    return [(p, c) for (p, c) in yaml_files if c == category]

# ================= POKEDEX YAML TESTS =================
# these tests iterate over all `pokedex_` YAMLs in data/
def test_pokedex_required_fields(yaml_files):
    """Tests whether all required fields are present for each Pokemon."""
    REQUIRED = {
        "name",
        "species_line",
        "evo_stage",
        "is_fully_evolved",
        "is_legendary",
        "types",
        "base_stat_total",
        "hm_learnset",
        "evolution_method_required"
    }
    for path, category in filter_yaml(yaml_files, "pokedex"):
        pokedex = load_yaml(path)
        for mon in pokedex:
            assert "name" in mon, "Pokemon must have a 'name' field" # check this first so we don't get a KeyError for name
            missing = REQUIRED - mon.keys()
            assert not missing, f"{path}: missing {missing} for {mon['name']}"

def test_pokedex_data_types(yaml_files):
    """Tests whether all data types are valid for each Pokemon."""
    valid_hms = {'CUT', 'FLASH', 'SURF', 'STRENGTH', 'FLY', 'DIG', 'TELEPORT', 'SOFTBOILED'}
    valid_types = {'normal', 'fire', 'water', 'grass', 'electric', 'flying', 'fighting',
                   'ice', 'psychic', 'ground', 'rock', 'poison', 'bug', 'dragon', 'ghost'}
    valid_evo_methods = {'none', 'level-up', 'moon_stone', 'fire_stone', 'water_stone',
                         'thunder_stone', 'leaf_stone', 'trade'}

    for path, category in filter_yaml(yaml_files, "pokedex"):
        pokedex = load_yaml(path)
        for mon in pokedex:
            # test name
            assert isinstance(mon["name"], str), f"{path}:{mon['name']}: 'name' must be a string"
            assert mon["name"].isupper(), f"{path}:{mon['name']}: 'name' must be uppercase"

            # test species_line
            assert isinstance(mon["species_line"], str), f"{path}:{mon['name']}: 'species_line' must be a string"

            # test evo_stage
            assert isinstance(mon["evo_stage"], int), f"{path}:{mon['name']}: 'evo_stage' must be an integer"

            # test is_fully_evolved
            assert isinstance(mon["is_fully_evolved"], bool), f"{path}:{mon['name']}: 'is_fully_evolved' must be a boolean"

            # test is_legendary
            assert isinstance(mon["is_legendary"], bool), f"{path}:{mon['name']}: 'is_legendary' must be a boolean"

            # test types
            assert isinstance(mon["types"], list), f"{path}:{mon['name']}: 'types' must be a list"
            assert all(isinstance(t, str) for t in mon["types"]), f"{path}:{mon['name']}: 'types' list must contain only strings"
            for t in mon["types"]:
                assert t in valid_types, f"{path}: Invalid type '{t}' for Pokemon '{mon['name']}'"

            # test base_stat_total
            assert isinstance(mon["base_stat_total"], int), f"{path}:{mon['name']}: 'base_stat_total' must be an integer"
            assert mon["base_stat_total"] > 0, f"{path}:{mon['name']}: 'base_stat_total' must be positive"

            # test hm_learnset
            assert isinstance(mon["hm_learnset"], list), f"{path}:{mon['name']}: 'hm_learnset' must be a list"
            assert all(isinstance(t, str) for t in mon["hm_learnset"]), f"{path}:{mon['name']}: 'hm_learnset' list must contain only strings"
            assert all(hm in valid_hms for hm in mon["hm_learnset"]), f"{path}:{mon['name']}: 'hm_learnset' list must contain only valid HMs"

            # test evolution_method_required
            assert isinstance(mon["evolution_method_required"], str), f"{path}:{mon['name']}: 'evolution_method_required' must be a string"
            assert mon["evolution_method_required"] in valid_evo_methods, f"{path}:Invalid evolution_method_required '{mon['evolution_method_required']}' for Pokemon '{mon['name']}'"

def test_location_fields(yaml_files):
    """Tests whether all fields in each location entry are valid."""
    valid_acquisition_methods = {'starter','walk','surf','old_rod','good_rod','super_rod','poke_flute',
                                 'static_encounter','trade','gift','purchase','fossil_restore','prize_window'}
    for path, category in filter_yaml(yaml_files, "locations"):
        locations = load_yaml(path)
        for location in locations:
            assert "map_name" in location
            assert isinstance(location["map_name"], str)
            assert all(field in valid_acquisition_methods for field in location if field != "map_name")
            for acquisition_method in location:
                if acquisition_method != 'map_name':
                    assert isinstance(location[acquisition_method], list)
                    assert all(isinstance(pokemon, str) for pokemon in location[acquisition_method])

def test_no_duplicate_location_fields(yaml_files):
    """Tests whether there are no duplicate location entries in a single locations YAML."""
    for path, category in filter_yaml(yaml_files, "locations"):
        unique_locations = []
        locations = load_yaml(path)
        for location in locations:
            assert location["map_name"] not in unique_locations, f"{path}: duplicate location entry {location['map_name']}"
            unique_locations.append(location["map_name"])

def test_meta_required_fields(yaml_files):
    """Tests whether all required fields are present in a meta YAML."""
    REQUIRED = {
        "starter_species",
        "modal_species",
        "limited_acquisition_methods",
        "acquisition_methods",
        "spheres",
        "sphere_generation_modes"
    }
    for path, category in filter_yaml(yaml_files, "meta"):
        meta = load_yaml(path)
        missing = REQUIRED - meta.keys()
        assert not missing, f"{path}: missing required fields {missing}"
