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
        self.name = name # str
        self.species_line = species_line # str
        self.evo_stage = evo_stage # int
        self.is_fully_evolved = is_fully_evolved # bool
        self.is_legendary = is_legendary # bool
        self.types = types # list[str]
        self.base_stat_total = base_stat_total # int
        self.hm_learnset = hm_learnset # list[str]
        self.evolution_method_required = evolution_method_required # str

    # def getParent() or something, which will get its next evo
    # def getChild() or something, which will get its previous evo

