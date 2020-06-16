def find_missing(lst):
    if lst:
        if not all(x for x in lst):
            return False
        nums = sorted(len(l) for l in lst)
        for i in range(nums[0], nums[-1] + 1):
            if i not in nums:
                return i
    return False