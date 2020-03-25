def loves_me(n):
    if n == 1:
        return 'Loves Me'.upper()

    phrases = ['Loves me,', 'Loves me not,']
    sentence = ''
    while True:
        for ph in phrases:
            sentence += ph + ' '
            n -= 1
            if n == 0:
                sentence = sentence.split(', ')[0:-1]
                sentence[-1] = sentence[-1].upper()
                return ', '.join(sentence)
