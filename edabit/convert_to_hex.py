def convert_to_hex(txt):
    return ' '.join(hex(ord(ch))[2:] for ch in txt)
