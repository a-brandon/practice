def topsy_turvy(lo, hi):
    mirrors, nums = {0: 0, 1: 1, 9: 6, 6: 9, 8: 8}, []

    for i in range(lo, hi + 1):
        l = int(''.join(str(mirrors.get(int(j), 0)) for j in str(i))[::-1])
        if l == i:
            nums.append(i)

    return nums