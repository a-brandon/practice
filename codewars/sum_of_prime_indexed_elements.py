def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def total(arr):
    return sum(x for i, x in enumerate(arr) if is_prime(i))