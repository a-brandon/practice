def parse_code(txt):
    t = txt.replace('0', ' ').split()
    decoded = ['first_name', 'last_name', 'id']
    return dict(zip(decoded, t))
