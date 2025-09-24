def min_terms(n):
    count = 0
    sum = 0
    for i in range(1, n):
        sum += (i**i)/(i+1)
        count += 1
        if sum > n:
            break
    return count

def fizzbuzz(max):
    for i in range(1, max+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

def print_square(side_length):
    for i in range(1, side_length+1):
        for j in range(1, side_length+1):
            if i == 1 or i == side_length or j == 1 or j == side_length:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_pyramid(height):
    for i in range(height+1, 1, -1):
        for j in range(1, i):
            print("*", end="")
            print(" ", end="")
        print()
        print(" " * (height+2-i), end="")