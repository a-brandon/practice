def find_missing(arr):
    if not arr:
        return False
    for elem in arr:
        if not elem:
            return False
    nums = sorted(len(elem) for elem in arr)
    for i, length in enumerate(nums, start=nums[0]):
        if i != length:
            return i
