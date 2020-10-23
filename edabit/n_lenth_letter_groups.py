def collect(s, n):
    return [] if len(s) < n else sorted(s[i: i + n] for i in range(0, len(s), n) if len(s[i: i + n]) == n)