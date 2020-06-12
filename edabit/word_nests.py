def valid_word_nest(word, nest):
    while len(nest) > len(word):
        if nest.count(word) > 1 or word not in nest:
            return False
        nest = nest.replace(word, '', 1)
    return True if nest == word else False


print(valid_word_nest("broadcast", "broadcbroadcastbroadcastast"))
