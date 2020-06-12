def is_alphabetically_sorted(sentence):
    s = ''.join(ch for ch in sentence if ch.isalpha() or ch.isspace()).lower().split()
    for word in s:
        if len(word) >= 3 and list(word) == sorted(word):
            return True
    return False



print(is_alphabetically_sorted("Beth dislikes eating starfruit but enjoys cherries."))