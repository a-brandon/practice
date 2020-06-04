def is_super_d(n):
    for i in range(2, 10):
        calc = str(i * (n ** i))
        if i * str(i) in calc:
            return 'Super-{} Number'.format(i)
    return 'Normal Number'
