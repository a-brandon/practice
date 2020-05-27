def is_icecream_sandwich(txt):
    if len(txt) < 3 or len(set(txt)) == 1:
        return False
    letter_count, letter = 0, txt[0]
    i = 0
    while txt[i] == letter:
        letter_count += 1
        i += 1
    s = txt[i:-i]
    return s == txt[i] * txt.count(txt[i])
