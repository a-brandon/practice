def solve(s):
    for c in s:
        if c not in 'aeiou':
            s = s.replace(c, ' ')
    return len(max(s.split(), key=len))