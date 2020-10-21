def solve(s):
    for ch in s:
        if not ch.isdigit():
            s = s.replace(ch, ' ')
    return max(s.split(), key=int)