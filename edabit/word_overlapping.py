def overlap(s1, s2):
    i = 0
    while i < len(s2):
        if s2.startswith(s1[i:]):
            return s1 + s2[len(s1[i:]):]
        i += 1
    return s1 + s2
