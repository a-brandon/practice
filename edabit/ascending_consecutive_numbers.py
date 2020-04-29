def is_consecutive(lst):
    return all(lst[i + 1] == lst[i] + 1 for i, _ in enumerate(lst[:-1]))


def ascending(txt):
    count, it, nums = 0, 1, []

    while count < len(txt):
        for i in range(len(txt)):
            group = txt[i * it: it * i + it]
            if group == txt:
                return False
            elif group:
                nums.append(int(txt[i * it: it * i + it]))
                
        if sorted(nums) == nums and is_consecutive(nums):
            return True
        else:
            nums = []
            it += 1
            count += 1
