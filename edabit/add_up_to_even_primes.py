def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def prime_pair_list(num):
    primes = [i for i in range(2, num) if is_prime(i)]
    pairs = []
    dupes = set()

    for x in primes:
        for y in primes:
            if x + y == num and x not in dupes and y not in dupes:
                pairs.append('{}+{}'.format(x, y))
                dupes.add(x)
                dupes.add(y)

    return pairs
