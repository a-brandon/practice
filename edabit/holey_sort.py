def holey_sort(lst):
    holes = {0: 1, 4: 1, 6: 1, 8: 2, 9: 1}
    nums = list(map(str, lst))
    ranks = {x: sum(holes.get(int(n), 0) for n in x) for x in nums}
    return list(map(int, sorted(ranks, key=ranks.get)))
