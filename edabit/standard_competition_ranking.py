def competition_rank(results, person):
    vals = sorted(results.values(), reverse=True)
    ranks = {x: vals.index(x) + 1 for x in vals}
    return ranks[results[person]]

