def numbers_to_ranges(lst):
    if lst == []:
        return []
    elif len(lst) == 1:
        return [str(lst[0])]

    ranges, nums = [], [lst[0]]
    for i in lst[1:]:
        if i - 1 != nums[-1]:
            f = '{}' if len(nums) == 1 else '{}-{}'
            ranges.append(f.format(nums[0], nums[-1]))
            nums = []
        nums.append(i)

    return ranges + ['{}-{}'.format(nums[0], nums[-1])]
