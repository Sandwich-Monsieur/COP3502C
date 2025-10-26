class Pakuri():
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}, {self.name}!")
    def attack(self, attack_name):
        print(f"{self.name} used {attack_name}!")

class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            print("Invalid amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("You don't have enough money :(")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}")

    def display(self):
        print(f"Current balance: ${self.balance}")

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
