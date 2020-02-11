def square_digits(n):
    numbers = list(str(n))
    return int(''.join([str(int(x) ** 2) for x in numbers]))
