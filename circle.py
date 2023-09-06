from math import pi

class Circle():
    def __init__(self, r):
        if not isinstance(r, (float, int)) or r <= 0:
            raise ValueError("Parameter r should be positive integer!")
        
        self.r = r

    def S(self):
        return pi * self.r * self.r
    
    def C(self):
        return 2 * pi * self.r
