class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = []

        for first_word in words:
            for second_word in words:
                if first_word in second_word and first_word != second_word:
                    l.append(first_word)

        return sorted(set(l))