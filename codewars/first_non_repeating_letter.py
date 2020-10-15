def first_non_repeating_letter(string):
    s = string.lower()

    if len(set(s)) == 1 and len(string) > 1:
        return ''

    non_repeats = {ch: i for i, ch in enumerate(s) if s.count(ch) == 1}
    if not non_repeats:
        return ''

    return string[non_repeats.get(min(non_repeats, key=non_repeats.get))]