def convert_to_decimal(perc: list) -> list:
    joined_string = ','.join(perc)
    split_string = joined_string.split(',')
    temp_list = [percent.strip('%') for percent in split_string]
    result = []
    for elem in temp_list:
        if elem.isdigit():
            result.append(int(elem) / 100)
        else:
            result.append(float(elem) / 100)
    return result
