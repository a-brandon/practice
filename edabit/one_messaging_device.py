from string import ascii_lowercase


def how_many_times(msg):
    alphabet_map = {alphabet: i for i, alphabet in enumerate(ascii_lowercase, start=1)}
    result = []
    for ch in msg:
        if ch in alphabet_map:
            result.append(alphabet_map[ch])
    return sum(result)
