class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        positions = dict(zip(indices, s))
        return ''.join(positions[i] for i in sorted(positions))