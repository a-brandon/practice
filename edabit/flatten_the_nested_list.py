def flatten(lst):
    l = str(lst).replace('[', '').replace(']', '').replace(' ', '')
    if l[0].isdigit():
        l = l.replace(',', ' ').split()
        return list(map(int, l))
    return [l.replace("'", '')]
