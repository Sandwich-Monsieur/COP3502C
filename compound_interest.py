principle = float(input("Initial principle: "))
interest_rate = float(input("Interest rate: "))
num_annual = int(input("How many times does interest apply annually: "))
years_passed = int(input("How many years have passed: "))

final_principle = principle * (1 + interest_rate / 100 / num_annual) ** (years_passed*num_annual)
final_principle = f"{final_principle:.2f}"
print("You now have $" + final_principle)