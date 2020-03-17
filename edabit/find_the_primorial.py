def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primorial(n):
    primes = [2]
    x = 3
    while len(primes) != n:
        if is_prime(x):
            primes.append(x)
            x += 1
        else:
            x += 1
    prod = 1
    for num in primes:
        prod *= num
    return prod
