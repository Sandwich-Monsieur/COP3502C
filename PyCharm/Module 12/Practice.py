################################# FRQ Question 1: #################################
#  Write a class PhoneBook that will store your contacts. It has three required methods:
#   1. add_contact(self, name, number) stores a contact in the phonebook
#   2. who_is(self, number) returns the name that matches the number parameter
#   3. get_number(self, name) returns the phone number that matches the name parameter
#
#   Example:
#   phonebook = PhoneBook()
#   phonebook.add_contact("alice", "012-345-6789")
#   phonebook.add_contact("bob", "111-222-3333")
#   print(phonebook.who_is("111-222-3333"))
#   print(phonebook.get_number("alice"))

# This would output:
# bob
# 012-345-6789

class PhoneBook():
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        self.contacts[number] = name

    def who_is(self, number):
        return self.contacts.get(number, "Contact not found.")

    def get_number(self, name):
        return self.contacts.get(name, "Contact not found.")

################################# FRQ Question 2: #################################
# For this problem, you will write a class that inherits from the class WordCounter.
# WordCounter has the following methods:
#       - add_word(self, word) adds a word to the class's counts
#       - print_counts(self) displays the counts for every word
# Write the class NonArticleCounter. It will inherit from class WordCounter, and modifies WordCounter's behavior in the following way:
#       - add_word() will only add the word if it is not "a", "an", or "the"
#       - print_counts() will print "This count excludes 'the', 'a', and 'an'" before printing out the word counts.

class WordCounter: # You do not need to modify this class.
    def __init__(self):
        self.word_counts = {}
    def add_word(self, word):
        word = word.lower()
        if word in self.word_counts:
            self.word_counts[word] += 1
        else:
            self.word_counts[word] = 1
    def print_counts(self):
        for word, count in self.word_counts.items():
            print(f"{word}: {count}")

class NonArticleCounter(WordCounter):
    def __init__(self):
        super().__init__()
        self.articles = ["a", "an", "the"]

    def add_word(self, word):
        if word.lower() not in self.articles:
            super().add_word(word)

    def print_counts(self):
        print("This count excludes 'the', 'a', and 'an'")
        super().print_counts()

################################# FRQ Question 3: #################################
# Create a program to model different types of electronic devices. Implement a base class called
# ElectronicDevice with the following attributes and methods:
# Attributes:
#     - brand (string): representing the manufacturer of the device
#     - model (string): representing the model of the device
#     - year (integer): representing the manufacturing year of the device
# Methods:
#     - Constructor: __init__(self, brand, model, year)
#     - display_info(self): method to display information about the device (brand, model, and year)
# Then, create a subclass called Laptop. Laptop should inherit from the ElectronicDevice class
# and contain an additional attribute: battery_life (integer) that represents battery life in hours.
# Additionally, Laptop should override the display_info function to include the battery life.
#
# Example:
# new_device = ElectronicDevice("Sony", "Walkman", 1995)
# new_device.display_info()
# Output:
# Brand: Sony
# Model: Walkman
# Year: 1995

class ElectronicDevice:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Laptop(ElectronicDevice):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Battery life: {self.battery_life} hours")

class student:
    grade = 85 #Class Attribute
    update = 10
    def __init__(self, age): #Constructor
        self.age = age #instance attribute
    def new_grade(self): #method inside class
        student.grade += student.update

Tom = student(20)
Tom.new_grade() #call method
print(Tom.grade) #once error is resolved, prints 95
