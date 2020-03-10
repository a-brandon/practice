def filter_primes(num):
    primes = []
    count = []
    for x in num:
        for i in range(2, x + 1):
            if x % i == 0:
                count.append(i)
        if len(count) == 1:
            primes.append(count[0])
            count = []
        else:
            count = []
    return primes
