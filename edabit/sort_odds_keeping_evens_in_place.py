def odd_sort(arr):
    odds = sorted(o for o in arr if o % 2)[::-1]
    nums = [n if n % 2 == 0 else '_' for n in arr]

    while odds:
        nums[nums.index('_')] = odds.pop()

    return nums
