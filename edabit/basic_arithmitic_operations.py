def arithmetic_operation(n):
    op_lookup = {'+': add_nums, '-': sub_nums, '//': divide_nums,
                 '*': multiply_nums}
    eq = [int(i) if i.isdigit() else i for i in n.split()]
    l, o, r = eq
    return op_lookup[o](l, r) if r > 0 else -1


def add_nums(x, y):
    return x + y


def sub_nums(x, y):
    return x - y


def divide_nums(x, y):
    return x // y


def multiply_nums(x, y):
    return x * y