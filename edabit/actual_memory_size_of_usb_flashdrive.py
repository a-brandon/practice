def actual_memory_size(MS):
    mem_size = int(MS[0:-2])
    actual_size = mem_size - ((7 / 100) * mem_size)

    if actual_size < 1:
        return '{}MB'.format(round(actual_size * 1000))

    if 'MB' in MS:
        return '{}{}'.format(int(actual_size), MS[-2:])
    return '{}{}'.format(round(actual_size, 2), MS[-2:])