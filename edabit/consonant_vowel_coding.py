def string_code(sentence):
    vowels, tally = 'aeiou', ['', '']
    for word in sentence.lower().split():
        tally[1] += str(sum(1 for c in word if c in vowels))
        tally[0] += str(sum(1 for c in word if c not in vowels and c.isalpha()))
    return [' '.join(x) for x in tally]
