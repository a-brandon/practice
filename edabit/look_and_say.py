def look_and_say(n):
    if len(str(n)) % 2 != 0:
        return 'invalid'
    n = str(n)
    nums = []
    for i, num in enumerate(n, start=1):
        if i % 2 == 0:
            nums.append(num * int(n[i - 2]))
    return int(''.join(nums))
