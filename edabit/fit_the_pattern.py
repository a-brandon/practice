def check_pattern(lst, pattern):
    if all(x == lst[0] for x in lst):
        return pattern.count(pattern[0]) == len(pattern)
    d = {}
    for a, b in zip(lst, pattern):
        d[b] = a
    for c in pattern:
        pattern = pattern.replace(c, str(d[c]))
    return ''.join(map(str, lst)) == pattern
