def pairs(ar):
    pairings = [ar[i: i + 2] for i in range(0, len(ar), 2) if len(ar[i: i + 2]) == 2]
    return sum(1 for x, y in pairings if x + 1 == y or y + 1 == x)