def flatten_list(lst):
    flat_list = []

    for e in lst:
        if isinstance(e, list):
            for elem in e:
                if isinstance(elem, list):
                    flat_list.extend(elem)
                else:
                    flat_list.append(elem)
        else:
            flat_list.append(e)

    return flat_list or []