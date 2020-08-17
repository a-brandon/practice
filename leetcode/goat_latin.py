class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()

        for i, w in enumerate(words):
            if w.lower().startswith(('a', 'e', 'i', 'o', 'u')):
                words[i] = f'{w}ma'
            else:
                words[i] = f'{w[1:]}{w[0]}ma'

            words[i] = '{}{}'.format(words[i], 'a' * (i + 1))

        return ' '.join(words)
