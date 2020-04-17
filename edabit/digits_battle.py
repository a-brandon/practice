def battle_outcome(num):
    n = list(map(int, str(num)))
    digits = []
    for i in range(len(n) // 2):
        pairs = n[i * 2:i * 2 + 2]
        if pairs[0] == pairs[1]:
            continue
        else:
            digits.append(max(pairs))
    if len(n) % 2 != 0:
        digits = digits + [n[-1]]
    return int(''.join(map(str, digits[:])))
