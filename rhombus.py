class Rhombus():
    def __init__(self, a, h):
        if not isinstance(a, (float, int)) or a <= 0:
            raise ValueError("Parameter a should be positive integer!")

        if not isinstance(h, (float, int)) or h <= 0:
            raise ValueError("Parameter h should be positive integer!")
        
        self.a = a
        self.h = h

    def S(self):
        return self.a * self.h

    def P(self):
        return self.a * 4
