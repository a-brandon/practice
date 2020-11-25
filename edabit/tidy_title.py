def tidy_books(lst):
    return [''.join(b).strip().split(' - ') for b in lst]