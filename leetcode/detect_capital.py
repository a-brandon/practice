class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if any(word.isupper() or word.islower() or word.istitle()):
            return True
        return False