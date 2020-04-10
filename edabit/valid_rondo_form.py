def valid_rondo(s):
    if s == 'A' or not (s.startswith('A') and s.endswith('A')):
        return False
    return all(i % 2 for i, c in enumerate(s, start=1) if c == 'A')
