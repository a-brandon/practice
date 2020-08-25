def mark_maths(lst):
    return '{}{}'.format(round((sum(eval(x.replace('=', '==')) for x in lst) / len(lst)) * 100), '%')