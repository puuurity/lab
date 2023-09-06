from math import sqrt

class Triangle():
    def __init__(self, a, b, c):
        for side in (a, b, c):
            if not isinstance(side, (int, float)) or side <= 0:
                raise ValueError("Parameters a, b, c should be positive integers!")
            
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Wrong triangle!")
        
        self.a = a
        self.b = b
        self.c = c

    def P(self):
        return self.a + self.b + self.c

    def S(self):
        p = self.P() / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
