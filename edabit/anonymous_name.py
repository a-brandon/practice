def is_correct_aliases(names, aliases):
    for name, alias in zip(names, aliases):
        letter = name[0]
        if alias.count(letter) != 2:
            return False
    return True
