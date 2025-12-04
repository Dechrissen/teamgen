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
            missing = REQUIRED - mon.keys()
            assert not missing, f"{path}: missing {missing} in {mon}"

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
            assert "name" in mon
            assert isinstance(mon["name"], str)
            assert mon["name"].isupper()

            # test species_line
            assert "species_line" in mon
            assert isinstance(mon["species_line"], str)

            # test evo_stage
            assert "evo_stage" in mon
            assert isinstance(mon["evo_stage"], int)

            # test is_fully_evolved
            assert "is_fully_evolved" in mon
            assert isinstance(mon["is_fully_evolved"], bool)

            # test is_legendary
            assert "is_legendary" in mon
            assert isinstance(mon["is_legendary"], bool)

            # test types
            assert "types" in mon
            assert isinstance(mon["types"], list), "'types' must be a list"
            assert all(isinstance(t, str) for t in mon["types"]), "'types' must contain only strings"
            for t in mon["types"]:
                assert t in valid_types, f"Invalid type '{t}' for Pokemon '{mon['name']}'"

            # test base_stat_total
            assert "base_stat_total" in mon
            assert isinstance(mon["base_stat_total"], int)
            assert mon["base_stat_total"] > 0

            # test hm_learnset
            assert "hm_learnset" in mon
            assert isinstance(mon["hm_learnset"], list)
            assert all(isinstance(t, str) for t in mon["hm_learnset"])
            assert all(hm in valid_hms for hm in mon["hm_learnset"])

            # test evolution_method_required
            assert "evolution_method_required" in mon
            assert isinstance(mon["evolution_method_required"], str)
            assert mon["evolution_method_required"] in valid_evo_methods, f"Invalid evolution method '{mon['evolution_method_required']}' for Pokemon '{mon['name']}'"

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

def test_location_pokemon_entries_are_valid(yaml_files):
    """Tests whether all Pokemon entries in each acquisition entry per map are also present in the Pokedex file for the same game."""
    #TODO don't know if we should do this
    pass
