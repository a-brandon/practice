from string import punctuation


def find_shortest_words(txt):
    new_string = ''
    for ch in txt:
        if ch not in punctuation:
            if not ch.isdigit():
                new_string += ch
    split_text = sorted(new_string.lower().split(), key=len)
    result = [split_text[0]]
    for word in split_text[1:]:
        if len(word) == len(result[0]):
            result.append(word)
    return sorted(result)
