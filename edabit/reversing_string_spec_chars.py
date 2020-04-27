def rev_specstring(n):
    letters = [c for c in n if c.isalpha()]
    x = list(n)
    for i, c in enumerate(x):
        if c.isalpha():
            x[i] = letters.pop()
    return ''.join(x)
