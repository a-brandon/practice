def average_ascii(txt):
    words = txt.split()
    char_codes = []
    for w in words:
        code_sum = sum(ord(c) for c in w)
        char_codes.append(code_sum)
    glob_avg = round(sum(char_codes) / len(char_codes), 2)
    return ' '.join(word.upper() if char_codes[i] > glob_avg else word for i, word in enumerate(words))
