def mode(nums):
    occurrences = {x: nums.count(x) for x in nums}
    return sorted(k for k, v in occurrences.items() if v == max(occurrences.values()))
