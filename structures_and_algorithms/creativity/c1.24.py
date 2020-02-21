def count_vowels(word: str) -> int:
    """C-1.24

    Write a short Python function that counts
    the number of vowels in a given string."""
    return sum([1 for i in word.lower() if i in ('a', 'e', 'i', 'o', 'u')])
