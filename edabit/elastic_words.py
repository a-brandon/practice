def odd_stretch(txt):
    s, indexes = [], []
    pivot = len(txt) // 2

    for i, ch in enumerate(txt):
        if i <= pivot:
            s.append((i + 1) * ch)
            indexes.append(i + 1)
        else:
            indexes[-1] -= 1
            s.append(indexes[-1] * ch)

    return ''.join(s)


def even_stretch(word):
    end = len(word) // 2
    s = []

    for i, ch in enumerate(word, start=1):
        if i <= end:
            s.append(i * ch)
        else:
            s.append(end * ch)
            end -= 1

    return ''.join(s)


def elasticize(word):
    if len(word) < 3:
        return word

    lengths = {0: even_stretch, 1: odd_stretch}
    return lengths[len(word) % 2](word)