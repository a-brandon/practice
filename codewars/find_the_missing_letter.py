def find_missing_letter(chars):
    for i in range(ord(chars[0]), ord(chars[-1]) + 1):
        letter = chr(i)
        if letter not in chars:
            return letter