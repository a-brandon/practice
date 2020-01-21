def count(deck):
    d = {'2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
         '7': 0, '8': 0, '9': 0,
         '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
    str_elems = [str(i) for i in deck]
    return sum(d[elem] for elem in str_elems)
