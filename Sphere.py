class Sphere:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        # can use this class to keep track of Location objects in sphere, as well as a list of inventory items for this sphere
        # probably ultimately create a dict of spheres, where the keys correspond to sphere number (int) and the value is the rest of the sphere info in a Sphere object