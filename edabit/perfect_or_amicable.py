def num_type(x):
    nums = sum(i for i in range(1, x) if x % i == 0)
    if nums == x:
        return 'Perfect'
    elif nums != x:
        total = sum(i for i in range(1, nums) if nums % i == 0)
        if total == x:
            return 'Amicable'
    return 'Neither'
