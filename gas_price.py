tank = input("How big is your car's gas tank: ")
current_tank = input("How many gallons are in your tank now: ")
price = input("What is the price of gas per gallon: ")

total = float(price) * (float(tank) - float(current_tank))

print("Your gas will cost $", round(total, 2), sep="")