def junction_or_self(n):
    junctions = []
    for i in range(n):
        digits = sum(int(x) for x in str(i))
        if digits + i == n:
            junctions.append(i)
    junctions.sort(reverse=True)
    return junctions or 'Self'
