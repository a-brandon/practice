def return_end_of_number(num: int)-> str:
    num_dict = {1: '-ST', 2: '-ND', 3: '-RD', 4: '-TH'}
    num_string = str(num)
    output = []
    for k, v in num_dict.items():
        if num_string.endswith(str(k)):
            output.append(num_string + v)
    return ''.join(output)
