class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(1 for s in words if not set(s) - set(allowed))