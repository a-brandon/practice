def count_substring(s):
    words = []
    for i, ch in enumerate(s):
        if ch == 'A':
            ends = [s[i:j + 1] for j, c in enumerate(s) if c == 'X' and j > i]
            words.extend(ends)
    return len(words)
