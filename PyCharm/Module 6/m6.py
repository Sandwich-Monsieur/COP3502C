def fourbonacci(n):
    if n < 5:
        if n == 1:
            return 1
        if n == 2:
            return 4
        if n == 3:
            return 7
        if n == 4:
            return 8
    else:
        f1 = 1
        f2 = 4
        f3 = 7
        f4 = 8
        n_term = 0
        for n in range(5, n+1):
            n_term = 4 * f1 + 3 * f2 + 2 * f3 + f4
            f1 = f2
            f2 = f3
            f3 = f4
            f4 = n_term
        return n_term

def odd_squares(n):
    count = 0
    a = 1
    while count < n:
        if a % 2 == 1:
            print(a**2)
            a +=2
        if (a**2 / a) == a:
            count += 1

def diamond(n):
    count = int(n/2)
    for i in range(1, n+1, 2):
        print(" " * count, end="")
        count -= 1
        for j in range(1, i+1):
            print(j, end="")
        print()
    count = 0
    for i in range(n-2, 0, -2):
        count += 1
        print(" " * count, end="")
        for j in range(1, i+1):
            print(j, end="")
        print()


