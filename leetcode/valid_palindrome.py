from string import punctuation


def find_palindrome(s):
    if not s:
        return True

    for c in punctuation:
        s = s.replace(c, ' ').lower()
    s = ''.join(s.split())

    return True if s == s[::-1] else False
