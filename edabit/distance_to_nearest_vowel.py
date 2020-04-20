def distance_to_nearest_vowel(txt):
    if len(set(txt)) == 1:
        return [0] * len(txt)

    dist = []
    for i, c in enumerate(txt):
        if c in 'aeiou':
            dist.append(0)
        else:
            vowels = [i for i, v in enumerate(txt) if v in 'aeiou']
            min_dist = min(abs(i - x) for x in vowels)
            dist.append(min_dist)

    return dist
