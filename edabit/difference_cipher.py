from typing import List


def encode_ciph(inpt: str) -> List[int]:
    cipher = [ord(inpt[0])]
    for i, c in enumerate(inpt[:-1]):
        diff = ord(inpt[i + 1]) - ord(inpt[i])
        cipher.append(diff)
    return cipher
