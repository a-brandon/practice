class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = {}

        for i in range(97, 123):
            n = i - 96
            if n >= 10:
                n = str(n) + '#'
            alpha[str(n)] = chr(i)

        m = []

        for i, ch in enumerate(s):
            if ch == '#':
                num = s[i - 2: i + 1]
                m.append(num)

        for ch in m:
            s = s.replace(ch, alpha[ch])

        for x in s:
            if not x.isalpha():
                s = s.replace(x, alpha[x])

        return s