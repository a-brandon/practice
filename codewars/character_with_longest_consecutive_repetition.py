def longest_repetition(chars):
    if not chars:
        return '', 0

    letters, runs = [chars[0]], []

    for ch in chars[1:]:
        if ch == letters[-1]:
            letters.append(ch)
        else:
            runs.append([letters[-1], len(letters)])
            letters = [ch]
    runs.append([ch, len(letters)])

    m = max(runs, key=lambda r: r[1])[1]

    for x, y in runs:
        if y == m:
            return x, y