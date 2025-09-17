price = float(input("Enter the price: "))
friday = str(input("Is it black friday [y/n]: "))
coupon = str(input("Do you have a coupon [y/n]: "))
employee = str(input("Do you have an employee discount [y/n]: "))

if friday == "y":
    price = price * 0.6
if coupon == "y":
    price = price * 0.95
if employee == "y":
    price = price * 0.8

print(f"The final price is: ${price:.2f}")