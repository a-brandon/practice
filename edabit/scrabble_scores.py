def best_words(lst):
    table = {'A': 1, 'B': 3, 'C': 3, 'D': 2,
             'E': 1, 'F': 4, 'G': 2, 'H': 4,
             'I': 1, 'J': 8, 'K': 5, 'L': 2,
             'M': 3, 'N': 1, 'O': 1, 'P': 3,
             'Q': 10, 'R': 1, 'S': 1, 'T': 1,
             'U': 1, 'V': 4, 'W': 4, 'X': 8,
             'Y': 4, 'Z': 10}
    scores = {word: 0 for word in lst}
    for word in lst:
        for letter in word:
            scores[word] += table[letter.upper()]
    scores = [k.lower() for k, v in scores.items() if v == max(scores.values())]
    return sorted(scores, key=lambda x: lst.index(x))

