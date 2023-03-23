class SimpleCalculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b!=0:
            return self.a/self.b
        else:
            raise ZeroDivisionError