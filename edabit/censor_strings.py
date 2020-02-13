def uncensor(txt, vowels):
    if len(vowels) == 0:
        return txt
    uncensored = ''
    vowels = list(vowels)
    while vowels:
        for c in txt:
            if c == '*':
                uncensored += vowels[0]
                vowels.pop(0)
            else:
                uncensored += c
    return uncensored
