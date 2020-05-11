def look_and_say(n):
    if len(str(n)) % 2:
        return 'invalid'
    nums = [str(n)[i: i + 2] for i in range(0, len(str(n)), 2)]
    return int(''.join(int(x) * y for x, y in nums))
