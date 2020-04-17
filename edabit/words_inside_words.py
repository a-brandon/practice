def word_groups(lst: list):
    group = {}
    for word in lst:
        matches = sorted(w for w in lst if word in w and w != word)
        if matches:
            group[word] = matches
    return group
