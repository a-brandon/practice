def max_ham(s1, s2):
    if sorted(s1) != sorted(s2):
        return False
    s1, s2 = s1.lower(), s2.lower()
    hamming_dist = 0
    for a, b in zip(s1, s2):
        if a != b:
            hamming_dist += 1
    return hamming_dist == len(s1) or hamming_dist
