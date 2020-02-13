def lengthen(s1, s2):
    if len(s1) > len(s2):
        output = ''
        while True:
            for char in s2:
                output += char
                if len(output) == len(s1):
                    return output
    else:
        output = ''
        while True:
            for char in s1:
                output += char
                if len(output) == len(s2):
                    return output
