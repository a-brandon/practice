def f(n):
    nums = {}

    for i in range(n - 1, 0, -1):
        primes = [j for j in range(2, i + 1) if i % j == 0]
        count = 0
        if len(primes) == 1:
            evens = [int(i) for i in list(str(i))]
            for num in evens:
                if num in [2, 4, 6, 8, 0]:
                    count += 1
            if count >= 1:
                nums[i] = count
    return max(nums, key=nums.get)

