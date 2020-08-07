def bitwise_one_zero(lst):
    parity_type = {1: 'odd', 0: 'even'}
    min_int = lst[0]
    result = {'@index 0': lst[0],
              'parity': parity_type[lst[0] % 2]}

    for i, x in enumerate(lst):
        if x < min_int:
            min_int = x
            result = {'@index {}'.format(i): x,
                      'parity': parity_type[x % 2]}

    return result