def is_correct_aliases(names, aliases):
    for a, b in zip(names, aliases):
        anons = b.split()
        if not (anons[0].startswith(a[0]) and anons[1].startswith(a[0])):
            return False
    return True
