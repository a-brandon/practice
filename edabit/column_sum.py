def col_with_max_sum(nums, n):
    cols = [nums[i * n: i * n + n] for i in range(len(nums) // n)]
    col_sums = [sum(col) for col in zip(*cols)]
    return col_sums.index(max(col_sums)) + 1
