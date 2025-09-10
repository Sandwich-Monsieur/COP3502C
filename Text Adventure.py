name = input("Choose your hero's name! ")
print("Your name will be:", name)

nameChange = input("Would you like to change your name? [y/n]: ")
while nameChange != "y" and nameChange != "n":
    print("Invalid input. Please try again~")
    nameChange = input("Would you like to change your name? [y/n]: ")

while nameChange == "y":
    name = input("Choose your hero's name! ")
    print("Your name will be:", name)
    nameChange = input("Would you like to change your name again? [y/n]: ")
    while nameChange != "y" and nameChange != "n":
        print("Invalid input. Please try again~")
        nameChange = input("Would you like to change your name again? [y/n]: ")


print("Hello", name + ".", "I understand your previous unwillingness to assist us with the quest,"
                           "but would you please reconsider it?")
choice = input("Do you wish to speak to the guildmaster or head to the market? ")