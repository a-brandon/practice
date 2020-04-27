def sum_consecutives(lst):
    nums = []
    for x in lst:
        idx = [i for i, num in enumerate(lst) if num == x]
        if all(idx[i] + 1 == idx[i + 1] for i, _ in enumerate(idx[:-1])) and lst.count(x) >= 2:
            check = x * len(idx)
            if check not in nums: nums.append(check)
        else:
            nums.append(x)
    return nums

