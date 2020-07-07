class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if not words:
            return 0

        table = [".-", "-...", "-.-.",
             "-..", ".", "..-.", "--.",
             "....", "..", ".---",
             "-.-", ".-..",
             "--", "-.", "---",
             ".--.", "--.-",
             ".-.", "...", "-",
             "..-", "...-", ".--",
             "-..-", "-.--", "--.."]
        letters = {c: m for c, m in zip(ascii_lowercase, table)}
        transformations = set()

        for w in words:
            translation = ''
            for ch in w:
                translation += letters[ch]
            transformations.add(translation)

        return len(transformations)