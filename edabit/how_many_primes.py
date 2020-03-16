def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_numbers(num):
    primes = []

    for i in range(2, num):
        if is_prime(i):
            primes.append(i)
    return len(primes)
