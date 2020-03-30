from collections import Counter


def color_pattern_times(cols):
    if len(cols) == 1:
        return 2
    freq = sum(Counter(cols).values()) * 2
    seconds = 0
    for i, _ in enumerate(cols[:-1]):
        if cols[i + 1] != cols[i]:
            seconds += 1
    return seconds + freq
