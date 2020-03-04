def filter_by_rating(d, rating):
    rates = {k: v for k, v in d.items() if v == rating}
    return rates if rates else 'No results found'
