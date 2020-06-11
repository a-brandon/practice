def expand(num):
    s = str(num)[::-1]
    l = [x + str(i * '0') for i, x in enumerate(s) if x != '0']
<<<<<<< HEAD
    return ' + '.join(l[::-1])
=======
    return ' + '.join(l[::-1])
>>>>>>> 7e313442b2bc3f2665d864aa820540829c145d16
