class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        return b == ('10' * len(b))[:len(b)]