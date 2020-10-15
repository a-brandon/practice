def remove_consecutive_duplicates(s):
    if not s:
        return ''

    s = s.split()
    words = [s[0]]
    for w in s[1:]:
        if w != words[-1]:
            words.append(w)

    return ' '.join(words)