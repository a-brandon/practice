def pigLatin(user_input):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if user_input[0] in vowels:
        return user_input + 'way'
    vowel_idx = 0
    for i, c in enumerate(user_input):
        if c in vowels:
            vowel_idx += i
            break
    return user_input[vowel_idx:] + user_input[0:vowel_idx] + 'ay'
