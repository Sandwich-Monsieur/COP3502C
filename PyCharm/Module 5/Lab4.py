def fibonacci(n):
    a = 0
    b = 1
    next_int = 0
    if n == 1:
        return 0
    if n > 1:
        for i in range(2, n):
            next_int = a + b
            a = b
            b = next_int
        return b

def is_prime(n):
    x = True
    if n < 0:
        x = False
    elif n == 1:
        return False
    elif n > 1:
        for i in range(2, n):
            if n % i == 0:
                x = False
    return x

def print_prime_factors(n):
    factors = []
    num = n
    for i in range(2, n+1):
        while num % i == 0:
            factors.append(str(i))
            num /= i
    string = " * ".join(factors)
    print(f"{n} = {string}")