def is_stretched(s1, s2):
    if s1 == s2:
        return True
    if len(set(s1) - set(s2)) == 1:
        return False
    counts = [s1.count(c) // 2 if s2.count(c) == 2 else s1.count(c) for c in s2]
    return all(i == counts[0] for i in counts[1:])
