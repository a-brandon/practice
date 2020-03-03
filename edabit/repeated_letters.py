def remove_repeats(s):
    rep = s[0]
    for c in s[1:]:
        if c != rep[-1]:
            rep += c
    return rep
