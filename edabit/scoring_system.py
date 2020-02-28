from string import ascii_lowercase, punctuation


def word_rank(txt):
    score_table = {letter: i for i, letter in enumerate(ascii_lowercase, start=1)}
    words = ''.join([c for c in txt if c not in punctuation and not c.isdigit()]).split()
    scores = []
    for word in words:
        div = list(word)
        nums = sum(score_table[letter.lower()] for letter in div)
        scores.append(nums)
    if scores.count(max(scores)) == 2:
        for i, _ in enumerate(scores):
            if scores[i] == max(scores):
                return words[i]
    return words[scores.index(max(scores))]
