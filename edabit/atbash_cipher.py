from string import ascii_lowercase

def atbash(txt):
    reg_alpha = ascii_lowercase
    rev_alpha = ascii_lowercase[::-1]
    cipher = []
    for letter in txt:
        if letter.isalpha() and letter.isupper():
            cipher.append(rev_alpha[reg_alpha.index(letter.lower())].upper())
        elif letter.islower() and letter.isalpha():
            cipher.append(rev_alpha[reg_alpha.index(letter)])
        else:
            cipher.append(letter)
    return ''.join(cipher)
