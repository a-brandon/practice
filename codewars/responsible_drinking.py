def hydrate(drink_string):
    total = sum(int(ch) for ch in drink_string if ch.isdigit())
    s = 'glasses' if total > 1 else 'glass'
    return f"{total} {s} of water"