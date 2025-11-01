class Sphere:
    def __init__(self,maps,items):
        self.maps = maps
        self.items = items

        # can use this class to keep track of Location objects in sphere, as well as a list of inventory items for this sphere
        # probably ultimately create a dict of spheres, where the keys correspond to sphere number (int) and the value is the rest of the sphere info in a Sphere object