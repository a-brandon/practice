def reverse(txt):
    chars = ['_' if c.isalpha() else c for c in txt]
    letters = sorted((c for c in txt if c.isalpha()), reverse=True)
    while letters:
        chars = ''.join(chars).replace('_', letters.pop(0), 1)
    return ''.join(chars)
