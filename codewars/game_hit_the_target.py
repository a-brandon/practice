def solution(mtrx):
    for e in mtrx:
        if '>' in e and 'x' in e:
            return e.index('x') > e.index('>')