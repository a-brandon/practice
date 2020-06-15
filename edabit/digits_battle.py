def battle_outcome(num):
    s = str(num)
    res = [max(s[i: i + 2]) for i in range(0, len(s), 2) if len(set(s[i: i + 2])) > 1]
    return int(''.join(res + [(s[-1])])) if len(s) % 2 else int(''.join(res))