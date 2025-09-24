def sum(*args):
    total = 0
    for i in args:
        total += i
    return float(total)

def print_range(x, y):
    for i in range(x, y):
        print(f"{i},", end=' ')
    print(y)

def sum_of_digits(num):
    sum = 0
    length = 0
    string = str(num)
    for char in str(num):
        length += 1
    for i in range(length):
        sum += int(string[i])
    return sum



