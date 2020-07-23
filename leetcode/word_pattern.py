class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(pattern) != len(str.split()):
            return False

        words = sorted(set(str.split()), key=str.index)
        letters = sorted(set(pattern), key=pattern.index)
        lookup = dict(zip(letters, words))

        for i, p in enumerate(pattern):
            if lookup.get(p, 0) != str.split()[i]:
                return False

        return True