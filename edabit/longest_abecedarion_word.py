def longest_abecedarian(lst):
    longest_word = ''
    for w in lst:
        alpha = [ord(c) - 96 for c in w]
        if alpha == sorted(alpha) and len(w) > len(longest_word):
            longest_word = w
    return longest_word