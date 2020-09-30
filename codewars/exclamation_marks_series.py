def remove(s):
    equal_marks = []

    for m in s.split():
        r = m.replace('!', '')
        m = min(m.split(r))
        equal_marks.append(f'{m}{r}{m}')

    return ' '.join(equal_marks)