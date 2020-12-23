def get_strings(city):
    unique_letters = set(c.lower() for c in city if c.isalpha())
    letters = sorted(unique_letters, key=lambda ch: city.lower().index(ch))
    return ','.join(f'{x}:{city.lower().count(x) * "*"}' for x in letters)