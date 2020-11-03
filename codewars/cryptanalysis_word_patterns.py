def word_pattern(word):
    pattern_lookup, code = {}, 0

    for c in word.lower():
        if c not in pattern_lookup:
            pattern_lookup[c] = str(code)
            code += 1

    return '.'.join(pattern_lookup[c.lower()] for c in word)