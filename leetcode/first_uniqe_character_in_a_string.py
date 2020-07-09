class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        letters = sorted((ch for ch in set(s) if s.count(ch) == 1), key=s.index)
        return s.index(letters[0]) if letters else -1