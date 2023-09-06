class Square():
    def __init__(self, a):
        if not isinstance(a, (float, int)) or a <= 0:
            raise ValueError("Parameter a should be positive integer!")

        self.a = a

    def S(self):
        return self.a * self.a
    
    def P(self):
        return self.a * 4
