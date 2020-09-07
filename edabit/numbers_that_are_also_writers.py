def is_autobiographical(n):
    s = str(n)
    return False if len(s) > 10 else all(s.count(str(i)) == int(num) for i, num in enumerate(s))