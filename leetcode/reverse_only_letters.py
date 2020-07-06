class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S:
            return S

        non_letters = [ch if not ch.isalpha() else 'rep' for ch in S]
        letters = [ch for ch in S if ch.isalpha()]
        if not letters:
            return S

        for i, ch in enumerate(non_letters):
            if ch == 'rep':
                non_letters[i] = letters.pop()

        return ''.join(non_letters)