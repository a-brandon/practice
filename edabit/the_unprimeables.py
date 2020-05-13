def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_unprimeable(num):
    if is_prime(num):
        return 'Prime Input'

    digits = [*range(10)]
    nums = [int(n) for n in str(num)]
    primes = []

    curr_num = num
    i, j = 0, 0

    while j < len(nums):
        nums[j] = digits[i]
        x = int(''.join(map(str, nums)))
        if is_prime(x):
            primes.append(x)
        i += 1
        if i == 10:
            j += 1
            i = 0
            nums = [int(i) for i in str(curr_num)]

    return sorted(primes) or 'Unprimeable'
