def longest_common_ending(txt1, txt2):
    ending = []
    txt1 = list(txt1)
    txt2 = list(txt2)
    while True:
        if txt1[-1] == txt2[-1]:
            ending.append(txt1[-1])
            txt1.pop(-1)
            txt2.pop(-1)
            if len(txt1) == 0 or len(txt2) == 0:
                break
        else:
            break
    ending = ''.join(ending[::-1])
    return ending if ending else ''
