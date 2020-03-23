def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def interprime(n):
    if is_prime(n):
        return []

    nums = []
    for i in range(n, 2, -1):
        if is_prime(i):
            nums.append(i)
            break

    prime = n + 1
    while True:
        if is_prime(prime) and prime > n:
            nums.append(prime)
            break
        prime += 1

    diff = n - nums[0]
    if n - nums[0] and n + diff == nums[-1]:
        return nums
    return []
