def shift_sentence(txt):
    words = txt.split()
    shifts = []
    for i, curr_word in enumerate(words):
        prev, curr_letters = words[i - 1], list(curr_word)
        curr_letters[0] = prev[0]
        shifts.append(''.join(curr_letters))
    return ' '.join(shifts)
