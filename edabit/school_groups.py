from string import ascii_lowercase


def print_all_groups():
    result = []
    for i in range(1, 7):
        for letter in ascii_lowercase[0:5]:
            result.append(str(i) + letter)
    return ', '.join(result)
