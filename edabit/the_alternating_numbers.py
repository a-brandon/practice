def is_alternating(num):
    if num <= 0:
        return False
    opps = {0: 'e', 1: 'o', 2: 'e', 3: 'o',
            4: 'e', 5: 'o', 6: 'e',
            7: 'o', 8: 'e', 9: 'o',
            10: 'e'}
    alts = [opps[x] for x in list(map(int, str(num)))]
    for i, c in enumerate(alts[:-1]):
        if alts[i] == alts[i + 1]:
            return False
    return True
