def string_letter_count(s):
    txt = sorted(ch for ch in set(s.lower()) if ch.isalpha())
    return ''.join(f'{s.lower().count(c)}{c}' for c in txt)