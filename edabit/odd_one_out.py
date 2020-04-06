from collections import Counter


def odd_one_out(lst):
    max_len = Counter(len(word) for word in lst)
    odd = 0
    for word in lst:
        if max_len[len(word)] != max(max_len.values()):
            odd += 1
    return True if odd == 1 else False
