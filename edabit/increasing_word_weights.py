from string import punctuation


def increasing_word_weights(sentence):
    words = ''.join(c for c in sentence if c not in punctuation).split()
    uni_sum = []
    for word in words:
        uni_sum.append(sum(ord(c) for c in word))
    return sorted(uni_sum) == uni_sum
