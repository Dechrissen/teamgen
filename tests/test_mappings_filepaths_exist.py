import yaml
from pathlib import Path
import pytest

# determine project root: one level up from tests/
ROOT = Path(__file__).resolve().parents[1]

# absolute path to mappings.yaml
MAPPINGS_PATH = ROOT / "data" / "mappings.yaml"

def load_mappings():
    with MAPPINGS_PATH.open() as f:
        return yaml.safe_load(f)

def collect_paths():
    """
    Returns a list of (game_name, file_type, path) tuples.
    Example:
    ("Red", "meta", Path("data/gen1/vanilla/meta_rb.yaml"))
    """
    mappings = load_mappings()
    results = []

    for game, files in mappings.items():
        for key, rel_path in files.items():
            p = Path(rel_path)
            results.append((game, key, p))

    return results

# create one test case per game/filetype/path tuple from collect_paths()
@pytest.mark.parametrize("game,file_type,path", collect_paths())
def test_paths_exist(game, file_type, path):
    """
    Ensures each mapped YAML file in mappings.yaml exists.
    """
    assert path.exists(), (
        f"Missing file for game {game!r}: {file_type} → {path} does not exist"
    )
