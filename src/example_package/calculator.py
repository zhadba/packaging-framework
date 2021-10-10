class Calculator():

    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        return self.number_1 + self.number_2

    def subtract(self):
        return self.number_1 - self.number_2

    def multiply(self):
        return self.number_1 * self.number_2

    def divide(self):
        return self.number_1 / self.number_2