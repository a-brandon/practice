def can_partition(nums):
    for i, x in enumerate(nums):
        prod = 1
        for j, n in enumerate(nums):
            if j != i:
                prod *= n
        if prod == x:
            return True
    return False
