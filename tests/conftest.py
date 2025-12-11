import yaml
from pathlib import Path
import pytest

BASE = Path(__file__).resolve().parents[1] # root of project

def find_yaml_files():
    """Yields (path, category) for all YAMLs in data/ subfolders."""
    for path in (BASE / "data").rglob("*.yaml"):
        name = path.name.lower()
        if "pokedex" in name:
            yield path, "pokedex"
        elif "locations" in name:
            yield path, "locations"
        elif "meta" in name:
            yield path, "meta"
        else:
            # unknown but still a valid YAML — skip these
            yield path, "unknown"

    for path in (BASE / "config").rglob("*.yaml"):
        name = path.name.lower()
        if "config" in name:
            yield path, "config"
        elif "global_settings" in name:
            yield path, "global_settings"
        else:
            # unknown but still a valid YAML — skip these
            yield path, "unknown"


@pytest.fixture(scope="session")
def yaml_files():
    """Returns a list of (path, category) tuples."""
    return list(find_yaml_files())


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)