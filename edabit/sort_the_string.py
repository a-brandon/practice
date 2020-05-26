from string import ascii_letters


def sorting(s):
    letters = sorted(sorted((c for c in s if c.isalpha()), key=ascii_letters.index), key=str.lower)
    nums = sorted(n for n in s if n.isdigit())
    return ''.join(letters + nums)
