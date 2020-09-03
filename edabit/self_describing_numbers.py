def self_descriptive(n):
    s = str(n)

    if len(s) % 2 != 0:
        return False

    for i in range(0, len(s), 2):
        x, y = s[i: i + 2]
        if s.count(y) != int(x):
            return False

    return True