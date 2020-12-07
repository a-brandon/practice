def in_array(array1, array2):
    subs = []

    for s in array1:
        for w in array2:
            if s in w and s not in subs:
                subs.append(s)

    return sorted(subs)