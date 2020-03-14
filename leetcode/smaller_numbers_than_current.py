def smaller_numbers(nums):
    res = []
    for x in nums:
        count = 0
        count += sum(1 for n in nums if n < x)
        res.append(count)
    return res
