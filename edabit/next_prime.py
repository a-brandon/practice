def next_prime(num):
    nums = [i for i in range(2, num + 1) if num % i == 0]
    if len(nums) == 1:
        return num
    while True:
        primes = []
        num += 1
        for i in range(2, num + 2):
            if num % i == 0:
                primes.append(i)
        if len(primes) == 1:
            return num
