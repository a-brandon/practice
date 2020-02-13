def split_groups(txt):
    output = ''
    for i in range(len(txt) - 1):
        output += txt[i]
        if txt[i + 1] != txt[i]:
            output += ','
    missing_el = output + txt[-1]
    sep_elements = missing_el.split(',')
    return sep_elements
