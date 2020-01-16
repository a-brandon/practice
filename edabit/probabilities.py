def probability(lst, n):
    return round(len([num for num in lst if num > n]) / len(lst) * 100, 1)
