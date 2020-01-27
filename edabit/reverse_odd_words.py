def reverse_odd(txt: string) -> string:
    result = []
    split_words = txt.split()
    for word in split_words:
        if len(word) % 2 != 0:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)
