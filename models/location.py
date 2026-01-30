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
                 prize_window: list[str] = None,
                 bug_catching_contest: list[str] = None,
                 squirt_bottle: list[str] = None,
                 headbutt:list[str] = None,
                 rock_smash: list[str] = None,
                 roaming: list[str] = None,
                 rainbow_wing: list[str] = None,
                 silver_wing: list[str] = None):
        ### acquisition methods ###
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
        self.bug_catching_contest = bug_catching_contest # list[str]
        self.squirt_bottle = squirt_bottle # list[str]
        self.headbutt = headbutt # list[str]
        self.rock_smash = rock_smash # list[str]
        self.roaming = roaming # list[str]
        self.rainbow_wing = rainbow_wing # list[str]
        self.silver_wing = silver_wing # list[str]
        #TODO add devon_scope for gen 3? (kecleon)

