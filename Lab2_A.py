side1 = float(input("Side length 1: "))
side2 = float(input("Side length 2: "))
side3 = float(input("Side length 3: "))

op1 = "This is an equilateral triangle!"
op2 = "This is an isosceles triangle!"
op3 = "This is a scalene triangle!"

if side1 == side2 and side2 == side3:
    print(op1)
elif side1 == side2 or side1 == side3 or side2 == side3:
    if side2 != side3 or side1 != side3 or side1 != side2:
        print(op2)
elif side1 != side2 and side2 != side3:
    print(op3)