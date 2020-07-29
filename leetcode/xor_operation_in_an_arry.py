class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        return eval(('{}^' * len(nums))[:-1].format(*nums))    