itemPrice = float(input("Enter the price of the item: "))
salesTax = float(input("Enter the sales tax percentage: "))

total = itemPrice * (1 + salesTax / 100)

print("Your total is $", f"{total:.2f}", sep="")