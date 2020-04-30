from string import ascii_lowercase


def nearest_vowel(s):
    alpha, vowels = ascii_lowercase, 'aeiou'
    vowel_idx = alpha.index(s)
    dist = {c: abs(alpha.index(c) - vowel_idx) for c in vowels}
    return sorted(k for k, v in dist.items() if v == min(dist.values()))[0]
