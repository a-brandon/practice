def group_by_commas(n):
    s = str(n)[::-1]
    chunks = [s[i:i + 3] for i in range(0, len(s), 3)]
    return ','.join(chunks)[::-1]