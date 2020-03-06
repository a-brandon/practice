def text_to_number_binary(txt):
    binary = {'zero': '0', 'one': '1'}
    binary_result = [binary[el] for el in txt.lower().split() if el in binary]
    while len(binary_result) % 8 != 0:
        binary_result.pop(-1)
    else:
        return ''.join(binary_result)
