def alternate_sort(lst):
    letters = sorted(c for c in lst if not isinstance(c, int))
    nums = sorted(n for n in lst if n not in letters)
    l = []
    for x, y in zip(nums, letters):
        l.extend([x, y])
    return l


print(alternate_sort([-2, "f", "A", 0, 100, "z"]))