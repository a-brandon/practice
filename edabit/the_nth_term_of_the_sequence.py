def seq(n):
    terms, count = [2, 6, 13, 23, 36, 52], 19
    while n > len(terms):
        terms.append(terms[-1] + count)
        count += 3
    return terms[n - 1] if n != 0 else 1
