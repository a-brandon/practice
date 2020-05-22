def make_number(n):
    seq = []

    for i in range(0, n):
        subs = []
        for j in range(i + 1, n):
            subs.append(j)
            if sum(subs) == n:
                seq.append(subs)
                break
            elif sum(subs) > n:
                break

    return seq
