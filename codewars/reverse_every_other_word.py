def reverse_alternate(s):
    words = s.split()
    rev_words = [w[::-1] for w in words[1::2]]
    words[1::2] = rev_words
    return ' '.join(words)