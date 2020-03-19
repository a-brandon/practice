def get_counts(txt):
    counts = 0
    for c in txt:
        if c == txt[0]:
            counts += 1
        else:
            break
    return counts


def is_icecream_sandwich(txt):
    s_length = len(txt) >= 3
    chars = len({ch for ch in txt}) == 2
    start, end = get_counts(txt), get_counts(txt[::-1])
    if not all((s_length, chars, start == end)):
        return False
    return True
