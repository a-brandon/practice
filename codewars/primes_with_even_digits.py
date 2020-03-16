def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def f(n):
    nums = {}

    for i in range(n - 1, 0, -1):
        if is_prime(i):
            evens = sum(1 for i in list(str(i)) if i in '2468')
            if evens >= 1:
                nums[i] = evens
    return max(nums, key=nums.get)
