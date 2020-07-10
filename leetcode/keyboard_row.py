class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if not words:
            return []

        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        output = []

        for w in words:
            for r in rows:
                if len(set(w.lower()) - set(r)) == 0:
                    output.append(w)
                    break

        return output