def character_mapping(txt):
    letters = sorted(set(txt), key=txt.index)
    return [letters.index(c) for c in txt]
