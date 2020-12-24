class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        counts = 0

        for e in mat:
            if sum(e) == 1:
                cols = [sum(col) for col in zip(*mat)]
                counts += 1 if cols[e.index(1)] == 1 else 0

        return counts