def get_length(lst):
    elems = []
    for x in lst:
        if not isinstance(x, int):
            s = str(x).replace('[', '').replace(']', '').split(',')
            elems.extend(s)
        else:
            elems.append(x)
    return len(elems)
