unit_from = input("Enter the unit you are converting from: ")
unit_to = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {unit_from}:"))

if unit_from == "Fahrenheit":
    if unit_to == "Celsius":
        temperature = (temperature - 32) * 5/9
    if unit_to == "Kelvin":
        temperature = (temperature - 32) * 5/9
        temperature = temperature + 273.15
elif unit_from == "Celsius":
    if unit_to == "Kelvin":
        temperature += 273.15
    if unit_to == "Fahrenheit":
        temperature = temperature * 9/5 + 32
elif unit_from == "Kelvin":
    if unit_to == "Celsius":
        temperature -= 273.15
    if unit_to == "Fahrenheit":
        temperature -= 273.15
        temperature = temperature * 9/5 + 32
print(f"That is {temperature:.1f} degrees {unit_to}.")