class Solution:
    def bitwiseComplement(self, N: int) -> int:
        comp = ['1' if b == '0' else '0' for b in bin(N)[2:]]
        return int(f'0b{"".join(comp)}', 2)