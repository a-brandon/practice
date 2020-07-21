class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        target_indices = [i for i, ch in enumerate(S) if ch == C]
        out = []

        for i, ch in enumerate(S):
            l = []

            for j in target_indices:
                l.append(abs(j - i))

            out.append(min(l))

        return out