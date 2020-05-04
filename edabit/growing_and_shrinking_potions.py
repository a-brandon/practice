def after_potion(txt):
    digits = [int(x) if x.isdigit() else x for x in txt]
    mixes = []
    for x, y in zip(digits, digits[1:]):
        if y == 'A':
            mixes.append(x + 1)
        elif y == 'B':
            mixes.append(x - 1)
        else:
            mixes.append(x)
    potions = ''.join(map(str, mixes)).replace('A', '').replace('B', '')
    last = str(digits[-1]) if str(digits[-1]) not in 'AB' else ''
    return potions + last

