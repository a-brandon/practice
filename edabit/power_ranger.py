def power_ranger(power, minimum, maximum):
    nums = [i for i in range(minimum, maximum + 1)]
    values = 0
    for i in range(1, len(nums) + 1):
        if i ** power in nums:
            values += 1
    return values
