def caesar_cipher(text, key):
    words = text.split()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = alpha + alpha
    for i, word in enumerate(words):
        letters = [alpha[alpha.find(c) + key] for c in list(word)]
        words[i] = ''.join(letters)
    return ' '.join(words)
