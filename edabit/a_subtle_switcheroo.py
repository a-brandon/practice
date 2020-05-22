from string import punctuation


def switcheroo(txt):
    switch = {'nts': 'nce', 'nce': 'nts'}
    s = txt.split()

    for i, word in enumerate(s):
        if word.lower().endswith('nts') or word.lower().endswith('nce'):
            s[i] = word.replace(word[-3:], switch[word[-3:]])
        elif ('nce' in word or 'nts' in word) and not word[-1].isalpha():
            punc = next(i for i, p in enumerate(word) if p in punctuation)
            if word[:punc].lower().endswith('nts') or word[:punc].lower().endswith('nce'):
                word, rem = word[:punc], word[punc:]
                s[i] = word.replace(word[-3:], switch[word[-3:]]) + rem

    return ' '.join(s)
