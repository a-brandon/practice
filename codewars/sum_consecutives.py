def sum_consecutives(s):
    totals, nums = [], [s[0]]

    for i in s[1:]:
        if i == nums[-1]:
            nums.append(i)
        else:
            totals.append(sum(nums))
            nums = [i]
    totals.append(sum(nums))

    return totals