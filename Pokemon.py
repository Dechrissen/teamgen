# needed for type hint annotation in methods, because otherwise there will be a type hint forward reference
# issue (the Pokemon class which is being referenced isn't defined yet)
from __future__ import annotations

class Pokemon:
    def __init__(self,
                 name: str,
                 species_line: str,
                 evo_stage: int,
                 is_fully_evolved: bool,
                 is_legendary: bool,
                 types: list[str],
                 base_stat_total: int,
                 hm_learnset: list[str],
                 evolution_method_required: str):
        self.name = name  # str
        self.species_line = species_line  # str
        self.evo_stage = evo_stage  # int
        self.is_fully_evolved = is_fully_evolved  # bool
        self.is_legendary = is_legendary  # bool
        self.types = types  # list[str]
        self.base_stat_total = base_stat_total  # int
        self.hm_learnset = hm_learnset  # list[str]
        self.evolution_method_required = evolution_method_required  # str

    def get_immediate_child(self, all_pokemon) -> Pokemon | None:
        """
        Returns the previous evolution of this Pokemon based on an input dict of all Pokemon.

        args:
            all_pokemon (dict of all Pokemon objects)

        returns:
            immediate_child (Pokemon object) or None
        """
        # save evolution stage
        stage = self.evo_stage

        # check if this is already a basic Pokemon, and return None if so
        if stage == 1:
            return None

        # save species
        species = self.species_line

        immediate_child = None

        # iterate through all Pokemon objects in all_pokemon dict,
        # checking if species is the same as this Pokemon and its evo_stage is one lower,
        # then save the previous evolution in immediate_child
        for mon in all_pokemon.keys():
            if all_pokemon[mon].species_line == species and all_pokemon[mon].evo_stage == (stage - 1):
                immediate_child = all_pokemon[mon]
                break

        return immediate_child

    def get_parent(self) -> Pokemon | None:
        # how would this work for branching evos like Eevee?
        # do we even need this?
        return