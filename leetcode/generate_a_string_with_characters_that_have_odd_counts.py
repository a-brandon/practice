class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * (n - 1) + 'b' if not n % 2 else 'a' * n