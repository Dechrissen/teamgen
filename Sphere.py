class Sphere:
    def __init__(self,
                 maps: list,
                 items: list):
        self.maps = maps # list
        self.items = items # list

        # method to build inventory? another to build pools?
        # (or no, there should be a separate function in Core that takes the all_spheres dict
        # and uses all their data to make the pools, since the function will need to access all
        # the spheres and not just one sphere itself)
