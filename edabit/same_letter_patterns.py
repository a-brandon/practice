def same_letter_pattern(txt1, txt2):
    if txt1 == txt2:
        return True

    pattern = [txt1.index(ch) for ch in txt1]
    pattern_2 = [txt2.index(ch) for ch in txt2]
    return pattern == pattern_2
