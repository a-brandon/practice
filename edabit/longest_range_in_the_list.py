def max_consec(lst):
    l, consec_nums, nums = sorted(set(lst)), [], []

    for i in range(l[0], l[-1] + 1):
        if i in l:
            nums.append(i)
        else:
            consec_nums.append(nums)
            nums = []

    consec_nums.append(nums)

    return len(max(consec_nums, key=len))
