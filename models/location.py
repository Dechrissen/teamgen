class Location:
    def __init__(self,
                 name: str,
                 starter: list[str] = None,
                 walk: list[str] = None,
                 surf: list[str] = None,
                 old_rod: list[str] = None,
                 good_rod: list[str] = None,
                 super_rod: list[str] = None,
                 poke_flute: list[str] = None,
                 static_encounter: list[str] = None,
                 trade: list[str] = None,
                 gift: list[str] = None,
                 purchase: list[str] = None,
                 fossil_restore: list[str] = None,
                 prize_window: list[str] = None):
        self.name = name # str
        self.starter = starter  # list[str]
        self.walk = walk # list[str]
        self.surf = surf # list[str]
        self.old_rod = old_rod # list[str]
        self.good_rod = good_rod # list[str]
        self.super_rod = super_rod # list[str]
        self.poke_flute = poke_flute # list[str]
        self.static_encounter = static_encounter # list[str]
        self.trade = trade # list[str]
        self.gift = gift # list[str]
        self.purchase = purchase  # list[str]
        self.fossil_restore = fossil_restore # list[str]
        self.prize_window = prize_window # list[str]
        #TODO add squirt_bottle for gen 2? sudowoodo
        #TODO add headbutt for gen 2?
        #TODO add devon_scope for gen 3? kecleon

