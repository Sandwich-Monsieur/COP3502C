import math
result = 0.0
choice_list = [0, 1, 2, 3, 4, 5, 6, 7]
num_calc = 0
sum_calc = 0.0
temp = 0

print(f"Current Result: {result}")

def print_options():
    print()
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")

def operands():
    operand1 = (input("Enter first operand: "))
    operand2 = (input("Enter second operand: "))
    return operand1, operand2
def add(x,y):
    if y == "RESULT":
        y = temp
        z = float(x) + y
        return z
    if x == "RESULT":
        x = temp
        z = x + float(y)
        return z
    z = float(x) + float(y)
    return z

def subtract(x,y):
    if y == "RESULT":
        y = temp
        z = float(x) - y
        return z
    if x == "RESULT":
        x = temp
        z = x - float(y)
        return z
    z = float(x) - float(y)
    return z

def mult(x,y):
    if y == "RESULT":
        y = temp
        z = float(x) * y
        return z
    if x == "RESULT":
        x = temp
        z = x * float(y)
        return z
    z = float(x) * float(y)
    return z

def div(x,y):
    if y == "RESULT":
        y = temp
        z = float(x) / y
        return z
    if x == "RESULT":
        x = temp
        z = x / float(y)
        return z
    z = float(x) / float(y)
    return z

def exp(x,y):
    if y == "RESULT":
        y = temp
        z = float(x) ** y
        return z
    if x == "RESULT":
        x = temp
        z = x ** float(y)
        return z
    z = float(x) ** float(y)
    return z

def log(x,y):
    if y == "RESULT":
        y = temp
        z = math.log(y, float(x))
        return z
    if x == "RESULT":
        x = temp
        z = math.log(float(y), x)
        return z
    z = math.log(float(y), float(x))
    return z

print_options()

while True:
    print()
    choice = int(input("Enter Menu Selection: "))
    if choice == choice_list[0]:
        print("Thanks for using this calculator. Goodbye!")
        exit()
    if choice == choice_list[1]:
        op1, op2 = operands()
        temp = add(op1, op2)
        num_calc += 1
        sum_calc += temp
        print("Current Result:", temp)
        print_options()
    if choice == choice_list[2]:
        op1, op2 = operands()
        temp = subtract(op1, op2)
        num_calc += 1
        sum_calc += temp
        print("Current Result:", temp)
        print_options()
    if choice == choice_list[3]:
        op1, op2 = operands()
        temp = mult(op1, op2)
        num_calc += 1
        sum_calc += temp
        print("Current Result:", temp)
        print_options()
    if choice == choice_list[4]:
        op1, op2 = operands()
        temp = div(op1, op2)
        num_calc += 1
        sum_calc += temp
        print("Current Result:", temp)
        print_options()
    if choice == choice_list[5]:
        op1, op2 = operands()
        temp = exp(op1, op2)
        num_calc += 1
        sum_calc += temp
        print("Current Result:", temp)
        print_options()
    if choice == choice_list[6]:
        op1, op2 = operands()
        temp = log(op1, op2)
        num_calc += 1
        sum_calc += temp
        print("Current Result:", temp)
        print_options()
    if choice == choice_list[7]:
        if num_calc == 0:
            print("Error: No calculations yet to average!")
        else:
            avg = sum_calc / num_calc
            print(f"Sum of calculations: {sum_calc:.2f}")
            print("Number of calculations:", num_calc)
            print(f"Average of calculations: {avg:.2f}")
    else:
        if choice > 7 or choice < 0:
            print("Error: Invalid selection!")