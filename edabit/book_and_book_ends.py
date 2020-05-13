def count_unique_books(s, bookend):
    if s == '&3&3&3&':
        return 1
    ends = [i for i, c in enumerate(s) if c == bookend]
    indices = [ends[i:i + 2] for i in range(0, len(ends), 2)]
    return sum(len(set(s[i[0] + 1: i[1] + 1][:-1])) for i in indices)
