def complete_binary(s):
    if len(s) % 8 == 0:
        return s
    s = list(s)
    while True:
        s[:0] += '0'
        if len(s) % 8 == 0:
            break
    return ''.join(s)
