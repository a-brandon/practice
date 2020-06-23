def is_metadrome(n):
    s = str(n)
    if len(set(s)) >= 2:
        return 'Metadrome' if list(s) == sorted(set(s)) else False
    return False


def is_plaindrome(n):
    s = str(n)
    if len(set(s)) >= 2:
        return 'Plaindrome' if list(s) == sorted(s) else False
    return False


def is_katadrome(n):
    s = str(n)
    if len(set(s)) >= 2:
        return 'Katadrome' if sorted(set(s), reverse=True) == list(s) else False
    return False


def is_nialpdrome(n):
    s = str(n)
    if len(set(s)) >= 2:
        return 'Nialpdrome' if sorted(s, reverse=True) == list(s) else False
    return False


def is_repdrome(n):
    return 'Repdrome' if len(set(str(n))) == 1 else False


def digitaldrome(n):
    return (is_metadrome(n) or is_plaindrome(n) or
            is_katadrome(n) or is_nialpdrome(n)
            or is_repdrome(n) or 'Nondrome')