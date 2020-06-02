def is_zygodrome(n):
    nums, count = set(str(n)), 0
    for num in nums:
        positions = [i for i, x in enumerate(str(n)) if x == num]
        if len(positions) < 2:
            return False
        count += 1 if all(positions[i] + 1 == positions[i + 1] 
                          for i, _ in enumerate(positions[:-1])) else 0
    return count == len(nums)
