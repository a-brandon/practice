def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def sum_primes(lst):
    return None if not lst else sum(x for x in lst if is_prime(x))