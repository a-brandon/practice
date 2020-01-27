def first_n_vowels(txt: str, n: int) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowel_string = ''
    for letter in txt:
        if letter in vowels:
            vowel_string += letter
    if len(vowel_string[0:n]) < n:
        return 'invalid'
    return vowel_string[0:n]
