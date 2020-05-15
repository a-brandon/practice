def will_fit(holds, cargo):
    d = {'L': 200, 'M': 100, 'S': 50}
    return all(d[h] >= c for h, c in zip(holds, cargo))
