from collections import Counter

def repeats(arr):
    counts = Counter()
    for i in arr:
        counts[i] += 1
    return sum(n for n in arr if counts[n] == 1)