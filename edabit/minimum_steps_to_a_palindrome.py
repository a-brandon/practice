def min_palindrome_steps(txt):
    if txt == txt[::-1]:
        return 0
    count = 0
    letters = []
    for c in txt:
        letters[:0] = c
        count += 1
        chars = txt + ''.join(letters)
        if chars == chars[::-1]:
            break
    return count
