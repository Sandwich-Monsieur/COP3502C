operation = str(input("Enter the operation: "))
operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))

if operation == "add":
    result = operand1 + operand2
elif operation == "sub":
    result = operand1 - operand2
elif operation == "mul":
    result = operand1 * operand2
elif operation == "div":
    result = operand1 / operand2

result = round(result, 2)
print(f"Result is {result}")