def mark_maths(lst):
    count = 0
    for expr in lst:
        expr = expr.split('=')
        if eval(expr[0]) == int(expr[-1]):
            count += 1
    per = str(round(count / len(lst) * 100))
    return per + '%'
