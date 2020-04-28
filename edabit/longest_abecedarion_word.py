from string import ascii_lowercase


def longest_abecedarian(lst):
    alpha = ascii_lowercase
    abecs = {}
    for word in lst:
        letters = [alpha.index(x) for x in word]
        if sorted(letters) == letters:
            abecs[word] = len(word)
    longest_abecs = [k for k, v in abecs.items() if v == max(abecs.values())]
    return longest_abecs[0] if longest_abecs else ''
