price = float(input("What is the listed price of the item: "))
paid = float(input("How much did the customer pay: "))

change = paid - price * 1.06
change = round(change, 2)
print("They get $", f"{change:.2f}", " in change", sep="")