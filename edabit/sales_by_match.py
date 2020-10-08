from collections import Counter


def sock_merchant(lst):
    counts = Counter()
    for i in lst:
        counts[i] += 1
    return sum(v // 2 if v % 2 == 0 else (v - 1) // 2 for v in counts.values())