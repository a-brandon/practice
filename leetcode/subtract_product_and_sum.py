class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        for i in str(n):
            prod *= int(i)

        return prod - sum(int(x) for x in str(n))