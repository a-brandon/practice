def kaprekar(num):
    count = 0
    while num != 6174:
        asc = int(''.join(sorted(str(num).zfill(4))))
        desc = int(''.join(sorted(str(num).zfill(4), reverse=True)))
        num = max(asc, desc) - min(asc, desc)
        count += 1
    return count
