class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = sorted(mat, key=lambda r: r.count(1))
        output = []
        i = 0

        while len(output) < k:
            r_idx = mat.index(rows[i])
            output.append(r_idx)
            mat[r_idx] = 0
            i += 1

        return output  