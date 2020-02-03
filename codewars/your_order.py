def order(sentence: str) -> str:
    """Your task is to sort a given string. 
    Each word in the string will contain a single number. 
    This number is the position the word should have in the result. """
    split_words = sentence.split()
    res = []
    for i in range(1, len(split_words) + 1):
        for word in split_words:
            if str(i) in word:
                res.append(word)
    return ' '.join(res)
