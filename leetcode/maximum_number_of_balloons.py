class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = 0

        while True:
            if any(c not in text for c in 'balloon'):
                return counter

            s = []

            for ch in 'balloon':
                if ch in text:
                    text = text.replace(ch, '', 1)
                    s.append(ch)

            if ''.join(s) == 'balloon':
                counter += 1
                s = []