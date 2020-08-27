class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total, chars_rep = 0, chars[:]

        for w in words:
            word_length = 0

            for c in w:
                if c in chars:
                    chars = chars.replace(c, '', 1)
                    word_length += 1

            if word_length == len(w):
                total += len(w)

            chars = chars_rep

        return total   