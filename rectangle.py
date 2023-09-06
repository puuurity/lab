class Rectange():
    def __init__(self, a, b):
        if not isinstance(a, (float, int)) or a <= 0:
            raise ValueError("Parameter a should be positive integer!")

        if not isinstance(b, (float, int)) or b <= 0:
            raise ValueError("Parameter b should be positive integer!")
        
        self.a = a
        self.b = b

    def S(self):
        return self.a * self.b
    
    def P(self):
        return (self.a + self.b) * 2
