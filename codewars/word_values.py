def name_value(my_list):
    alphabet_lookup = {chr(i): ord(chr(i)) - 96 for i in range(ord('a'), ord('z') + 1)}

    res = []
    for i, s in enumerate(my_list, start=1):
        total = sum(alphabet_lookup[ch] for ch in s if ch.isalpha()) * i
        res.append(total)

    return res