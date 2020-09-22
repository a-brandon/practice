def next_higher(value):
    val_bits = bin(value)[2:].count('1')
    x = value + 1

    while True:
        x_bits = bin(x)[2:].count('1')

        if x_bits == val_bits:
            return x
        else:
            x += 1