def inatorInator(inv):
    consonants = [chr(letter) for letter in range(ord('a'), ord('z')+1) if chr(letter) not in ['a', 'e', 'i', 'o', 'u']]
    if inv[-1] in consonants:
        return f'{inv}inator {len(inv)}000'
    else:
        return f'{inv}-inator {len(inv)}000'
