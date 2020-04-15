def can_complete(initial, word):
    return ''.join(sorted(set(c for c in word if c in initial), key=lambda c: word.index(c))) == initial
