def edabit_in_string(txt):
    if not all(c in txt for c in 'edabit'):
        return 'NO'

    prev, word = ['e'], 'dabit'
    for i, c in enumerate(word):
        curr = [i for i, c in enumerate(txt) if c == prev[-1]]
        next_letter = [i for i, x in enumerate(txt) if x == c]
        if any(c > x for c in next_letter for x in curr):
            prev.append(c)
    return 'YES' if ''.join(prev) == 'edabit' else 'NO'
