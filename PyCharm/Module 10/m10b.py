from base_classes import *

class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self._password = password

    def get_balance(self, password):
        if password != self._password:
            print("Incorrect password")
            return
        return super().get_balance()

    def deposit(self, amount, password):
        if password != self._password:
            print("Incorrect password")
            return
        super().deposit(amount)

    def withdraw(self, amount, password):
        if password != self._password:
            print("Incorrect password")
            return
        super().withdraw(amount)

class MemoryCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.prev_result = 0

    def _resolve(self, val):
        return self.prev_result if val == "RESULT" else val

    def add(self, x, y):
        x = self._resolve(x)
        y = self._resolve(y)
        self.prev_result = super().add(x, y)
        return self.prev_result

    def sub(self, x, y):
        x = self._resolve(x)
        y = self._resolve(y)
        self.prev_result = super().sub(x, y)
        return self.prev_result

class ImprovedFraction(Fraction):
    def add(self, other):
        if type(other) == int:
            return super().add(ImprovedFraction(other, 1))
        return super().add(other)

    def multiply(self, other):
        if type(other) == int:
            return super().multiply(ImprovedFraction(other, 1))
        return super().multiply(other)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"{self.get_numerator()}/{self.get_denominator()}"
