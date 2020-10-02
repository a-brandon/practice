def shortest_to_char(s, c):
    if not s or not c:
        return []
    if c not in s:
        return []


    min_dists = []
    for i, _ in enumerate(s):
        shortest_dist = []
        for j, target in enumerate(s):
            if target == c:
                shortest_dist.append(abs(i - j))
        min_dists.append(min(shortest_dist))

    return min_dists