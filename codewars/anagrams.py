def anagrams(word, words):
    """Write a function that will find all the anagrams of a word from a list. 
    You will be given two inputs a word and an array with words. 
    You should return an array of all the anagrams or an empty array if there are none."""
    return [el for el in words if sorted(el) == sorted(word)]
