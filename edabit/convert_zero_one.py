def text_to_number_binary(txt):
    txt = txt.lower().split()
    binary = {'zero': '0', 'one': '1'}
    binary_result = []
    for el in txt:
        if el in binary:
            binary_result.append(binary[el])
    while len(binary_result) % 8 != 0:
        binary_result.pop(-1)
    else:
        return ''.join(binary_result)
